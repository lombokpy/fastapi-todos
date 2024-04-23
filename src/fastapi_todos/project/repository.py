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

    def get_multi(self, *, skip: int = 0, limit: int = 0) -> List[domain.Project]:
        return self.session(models.Project).offset(skip).limit(limit).all()

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