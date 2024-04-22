from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from uuid import UUID
from typing import Optional, List
from datetime import datetime
from shared import entity
from user.domain import User


@dataclass
class Project:
    id: UUID = field(default=None)
    name: Optional[str] = field(default=None)
    created_at: Optional[datetime] = field(default=None)
    updated_at: Optional[datetime] = field(default=None)
    user_id: Optional[UUID] = field(default=None)
    user: Optional[User] = field(default=None)


@dataclass
class BaseProjectReponse(entity.BaseResponse):
    data: Project = field(default=None)


@dataclass
class BaseListProjectReponse(entity.BaseListResponse):
    data: List[Project] = field(default=None)


class ProjectRepositoryBase(ABC):

    @abstractmethod
    def get(self, *, id: UUID) -> Project:
        pass

    @abstractmethod
    def get_multi(self, *, skip: int = 0, limit: int = 0) -> List[Project]:
        pass

    @abstractmethod
    def create(self, *, obj_in: Project, user_id: UUID) -> Project:
        pass

    @abstractmethod
    def remove(self, *, id: UUID) -> Project:
        pass

    @abstractmethod
    def update(self, *, db_obj: Project, obj_id: Project) -> Project:
        pass