from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from uuid import UUID
from typing import Optional, List
from datetime import datetime
from shared import entity
from project.domain import Project


@dataclass
class Todo:
    id: UUID = field(default=None)
    title: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)
    done: Optional[bool] = field(default=None)
    started_at: Optional[datetime] = field(default=None)
    ended_at: Optional[datetime] = field(default=None)
    created_at: Optional[datetime] = field(default=None)
    updated_at: Optional[datetime] = field(default=None)
    project_id: Optional[UUID] = field(default=None)
    project: Optional[Project] = field(default=None)


@dataclass
class BaseTodoReponse(entity.BaseResponse):
    data: Todo = field(default=None)


@dataclass
class BaseListTodoReponse(entity.BaseListResponse):
    data: List[Todo] = field(default=None)


class TodoRepositoryBase(ABC):

    @abstractmethod
    def get(self, *, id: UUID) -> Todo:
        pass

    @abstractmethod
    def get_multi(self, *, skip: int = 0, limit: int = 0, project_id: UUID) -> List[Todo]:
        pass

    @abstractmethod
    def create(self, *, obj_in: Todo, project_id: UUID) -> Todo:
        pass

    @abstractmethod
    def remove(self, *, id: UUID) -> Todo:
        pass

    @abstractmethod
    def update(self, *, db_obj: Todo, obj_in: Todo) -> Todo:
        pass

    @abstractmethod
    def count(self, *, project_id: UUID) -> int:
        pass

    @abstractmethod
    def done(self, *, obj_in: Todo) -> Todo:
        pass

    def start(self, *, obj_in: Todo) -> Todo:
        pass

    def stop(self, *, obj_in: Todo) -> Todo:
        pass

