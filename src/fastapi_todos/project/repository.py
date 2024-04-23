from typing import List, Optional
from project import domain
from sqlalchemy.orm import Session
from uuid import UUID
from dbase import models


class ProjectRepository(domain.Project):
    def __init__(self, session: Session):
        self.session = session

    def get(self, *, id: UUID) -> domain.Project:
        db_obj: models.Project = self.session.query(models.Project).filter(models.Project.id == id).first()
        return db_obj.to_entity()

    def get_multi(self, *, skip: int = 0, limit: int = 0, user_id: UUID) -> List[domain.Project]:
        projects = self.session.query(models.Project).filter(
            models.Project.user_id == user_id
        ).offset(skip).limit(limit).all()
        list_project = [p.to_entity() for p in projects]
        return list_project

    def create(self, *, obj_in: domain.Project, user_id: UUID) -> domain.Project:
        db_obj = models.Project(name=obj_in.name, user_id=user_id)
        self.session.add(db_obj)
        self.session.commit()
        return db_obj.to_entity()

    def update(self, *, id: UUID, obj_in: domain.Project) -> domain.Project:
        db_obj = self.get(id=id)
        db_obj.id = obj_in.id
        


    def remove(self):
        ...

    def count(self, user_id: UUID):
        total = self.session.query(models.Project).filter(models.Project.user_id == user_id).count()
        return total