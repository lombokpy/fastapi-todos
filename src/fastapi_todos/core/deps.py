import logging
from typing import Generator
from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from auth import schemas as auth_schemas
from core import security
from core.config import settings
from dbase import models
from dbase.session import SessionLocal
from user import repository

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)

log = logging.getLogger("uvicorn")


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_user_repo(
    db: Session = Depends(get_db),
):
    return repository.UserV2Repository(db)


def get_current_user(
    db: Session = Depends(get_db),
    user_repo: repository.UserV2Repository = Depends(get_user_repo),
    token: str = Depends(reusable_oauth2),
) -> models.User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = auth_schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )

    id_uuid = UUID(token_data.sub)
    user = user_repo.get(id=id_uuid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_current_active_user(
    user_repo: repository.UserV2Repository = Depends(get_user_repo),
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not user_repo.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_current_active_superuser(
    user_repo: repository.UserV2Repository = Depends(get_user_repo),
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not user_repo.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user
