from typing import Optional, List
from project import domain
from uuid import UUID


class ProjectUsecase:
    def __init__(self, repo: domain.ProjectRepositoryBase):
        self.repo = repo

    def get_multi(self, skip: int = 0, limit: int = 100) -> List[domain.Project]:
        return self.repo.get_multi(skip=skip, limit=limit)
    
    def create(self, *, obj_in: domain.Project, user_id: UUID) -> domain.Project:
        project = self.repo.create(obj_in=obj_in, user_id=user_id)
        return project