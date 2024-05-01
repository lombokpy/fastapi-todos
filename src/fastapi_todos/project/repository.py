import dataclasses
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
        if not db_obj:
            return None
        return db_obj.to_entity()

    def get_multi(self, *, skip: int = 0, limit: int = 0, user_id: UUID) -> List[domain.Project]:
        projects = self.session.query(models.Project).filter(
            models.Project.user_id == user_id
        ).offset(skip).limit(limit).all()
        list_project = []
        for p in projects:
            project: models.Project = p.to_entity()
            list_project.append(project)
        return list_project

    def create(self, *, obj_in: domain.Project, user_id: UUID) -> domain.Project:
        db_obj = models.Project(name=obj_in.name, user_id=user_id)
        self.session.add(db_obj)
        self.session.commit()
        return db_obj.to_entity()

    def update(self, *, id: UUID, obj_in: domain.Project) -> domain.Project:
        db_obj: models.Project = self.session.query(models.Project).filter(models.Project.id == id).first()
        if not db_obj:
            raise Exception("Project not found")
        
        for field in dataclasses.fields(obj_in):
            value = getattr(obj_in, field.name)
            if value is not None:
                setattr(db_obj, field.name, value)
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return db_obj.to_entity()

    def remove(self, id: UUID) -> domain.Project:
        db_obj: models.Project = self.session.query(models.Project).filter(models.Project.id == id).first()
        self.session.delete(db_obj)
        self.session.commit()
        return db_obj.to_entity()

    def count(self, user_id: UUID):
        total = self.session.query(models.Project).filter(models.Project.user_id == user_id).count()
        return total