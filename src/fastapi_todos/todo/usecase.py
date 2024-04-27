from typing import Optional, List
from todo import domain
from uuid import UUID
from shared import paginator


class TodoUsecase:
    def __init__(self, repo: domain.TodoRepositoryBase):
        self.repo = repo

    def create_todo(self, *, obj_in: domain.Todo, project_id: UUID) -> domain.Todo:
        return self.repo.create(obj_in=obj_in, project_id=project_id)
    
    def get_todo(self, *, id: UUID) -> domain.Todo:
        return self.repo.get(id=id)
    
    def get_multi(self, *, skip: int = 0, limit: int = 0, project_id: UUID) -> List[domain.Todo]:
        total = self.repo.count(project_id=project_id)
        todos = self.repo.get_multi(skip=skip, limit=limit, project_id=project_id)
        pagination = paginator.paginate_data(total=total, skip=skip, limit=limit)
        return domain.BaseListTodoReponse(
            status=200, data=todos, pagination=pagination, message="Success"
        )