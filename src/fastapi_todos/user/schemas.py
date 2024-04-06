from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr

from user import domain
from shared import schemas


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None

    def to_entity(self) -> domain.User:
        en = domain.User(
            email=self.email,
            full_name=self.full_name or "",
            is_active=self.is_active,
            is_superuser=self.is_superuser,
        )
        if hasattr(self, "id"):
            en.id = self.id
        if hasattr(self, "hashed_password"):
            en.hashed_password = self.hashed_password
        if hasattr(self, "password"):
            en.password = self.password
        return en


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[UUID] = None
    model_config = ConfigDict(from_attributes=True)


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str


class ListUserResponse(schemas.BaseListResponse):
    data: List[User]