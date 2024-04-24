import dataclasses
from typing import List, Optional
from project import domain
from sqlalchemy.orm import Session
from uuid import UUID
from dbase import models
from todo import domain


class TodoRepository(domain.Todo):
    def __init__(self, session: Session):
        self.session = session

    def get(self, *, id: UUID) -> domain.Todo:
        pass

    def get_multi(self, *, skip: int = 0, limit: int = 0, project_id: UUID) -> List[domain.Todo]:
        pass

    def create(self, *, obj_in: domain.Todo, project_id: UUID) -> domain.Todo:
        db_obj = models.Todo(title=obj_in.title, description=obj_in.description, project_id=project_id)
        self.session.add(db_obj)
        self.session.commit()
        return db_obj.to_entity()
