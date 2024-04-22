from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core import deps
from project import usecase, repository, schemas
from typing import Any
from dbase import models
from dataclasses import asdict


router = APIRouter()


def project_usecase(session: Session = Depends(deps.get_db)):
    repo = repository.ProjectRepository(session)
    ucase = usecase.ProjectUsecase(repo)
    return ucase


@router.post("/")
def create_project(
    project_in: schemas.ProjectCreate,
    db: Session = Depends(deps.get_db),
    ucase: usecase.ProjectUsecase = Depends(project_usecase),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    obj_in = project_in.to_entity()
    project = ucase.create(user_id=current_user.id, obj_in=obj_in)
    project = schemas.ProjectBase(**asdict(project))
    project_schema_reponse = schemas.ProjectCreateReponse(
        status = 200,
        message="success",
        data=project
    )
    return project_schema_reponse