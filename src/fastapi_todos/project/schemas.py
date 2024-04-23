from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict
from project import domain
from shared import schemas
from datetime import datetime


class ProjectBase(BaseModel):
    id: Optional[UUID] = None
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class ProjectCreate(BaseModel):
    name: str

    def to_entity(self) -> domain.Project:
        en = domain.Project(name=self.name)
        if hasattr(self, "id"):
            en.id = self.id
        if hasattr(self, "created_at"):
            en.created_at = self.created_at
        if hasattr(self, "updated_at"):
            en.updated_at = self.updated_at
        return en
    
    
class ProjectGetRequest(ProjectCreate):
    pass


class ProjectCreateReponse(schemas.BaseResponse):
    data: ProjectBase


class ProjectResponse(schemas.BaseResponse):
    data: ProjectBase