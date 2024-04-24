from typing import Optional, List
from todo import domain
from uuid import UUID


class TodoUsecase:
    def __init__(self, repo: domain.TodoRepositoryBase):
        self.repo = repo

    def create_todo(self, *, obj_in: domain.Todo, project_id: UUID) -> domain.Todo:
        return self.repo.create(obj_in=obj_in, project_id=project_id)