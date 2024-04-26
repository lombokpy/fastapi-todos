from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict
from todo import domain
from shared import schemas
from datetime import datetime


class TodoBase(BaseModel):
    id: Optional[UUID] = None
    title: Optional[str] = None
    description: Optional[str] = None
    done: Optional[bool] = None
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    project_id: UUID


class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    started_at: Optional[datetime] = None

    def to_entity(self) -> domain.Todo:
        en = domain.Todo(
            title=self.title,
            description=self.description
        )
        if hasattr(self, "id"):
            en.id = self.id
        if hasattr(self, "created_at"):
            en.created_at = self.created_at
        if hasattr(self, "updated_at"):
            en.updated_at = self.updated_at
        return en


class TodoInDb(BaseModel):
    id: Optional[UUID] = None
    title: Optional[str] = None
    description: Optional[str] = None
    done: Optional[bool] = None
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
    project_id: UUID


class TodoCreateResponse(schemas.BaseResponse):
    data: TodoInDb