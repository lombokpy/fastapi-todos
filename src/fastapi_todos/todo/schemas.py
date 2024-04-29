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
        )
        if hasattr(self, "id"):
            en.id = self.id
        if hasattr(self, "created_at"):
            en.created_at = self.created_at
        if hasattr(self, "updated_at"):
            en.updated_at = self.updated_at
        return en


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

    def to_entity(self):
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


class TodoDoneRequest(BaseModel):
    done: Optional[bool] = None

    def to_entity(self):
        en = domain.Todo(
            done=self.done
        )
        return en
    

class TodoStartedAtRequest(BaseModel):
    started_at: Optional[datetime] = None

    def to_entity(self):
        en = domain.Todo(
            started_at=self.started_at
        )
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


class TodoGetResponse(schemas.BaseResponse):
    data: TodoInDb


class TodoListResponse(schemas.BaseListResponse):
    data: List[TodoInDb]


class TodoUpdateResponse(schemas.BaseResponse):
    data: TodoInDb


class TodoDeleteResponse(schemas.BaseResponse):
    data: Optional[str] = None


class TodoDoneReponse(schemas.BaseResponse):
    data: TodoInDb


class TodoStartedAtReponse(TodoDoneReponse):
    pass