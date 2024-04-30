from typing import Optional, List
from project import domain
from uuid import UUID
from shared import exceptions, paginator
from dbase import models
from project import schemas
from dataclasses import asdict


class ProjectUsecase:
    def __init__(self, repo: domain.ProjectRepositoryBase):
        self.repo = repo

    def get_multi(
            self, skip: int, limit: int,
            user_id: UUID
    ) -> domain.BaseListProjectReponse:
        total = self.repo.count(user_id=user_id)
        projects = self.repo.get_multi(skip=skip, limit=limit, user_id=user_id)
        pagination = paginator.paginate_data(total=total, skip=skip, limit=limit)
        return domain.BaseListProjectReponse(
            status=200, data=projects, pagination=pagination, message="Success"
        )
    
    def create(self, *, obj_in: domain.Project, user_id: UUID) -> domain.Project:
        project = self.repo.create(obj_in=obj_in, user_id=user_id)
        return project
    
    def get_project_by_id(self, *, project_id: UUID) -> Optional[domain.Project]:
        project: models.Project = self.repo.get(id=project_id)
        # list_project = [schemas.ProjectInDB(**asdict(p.to_entity())) for p in projects]
        return project

    def update(self, *, id: UUID, obj_in: domain.Project) -> domain.Project:
        project = self.repo.update(id=id, obj_in=obj_in)
        return project
    
    def delete_project(self, *, id: UUID) -> domain.Project:
        return self.repo.remove(id=id)