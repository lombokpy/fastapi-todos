from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core import deps
from project import usecase, repository, schemas
from typing import Any
from dbase import models
from dataclasses import asdict
import uuid
from shared import exceptions


router = APIRouter()


def project_usecase(session: Session = Depends(deps.get_db)):
    repo = repository.ProjectRepository(session)
    ucase = usecase.ProjectUsecase(repo)
    return ucase


@router.post("/")
def create_project(
    project_in: schemas.ProjectCreate,
    db: Session = Depends(deps.get_db),
    ucase: usecase.ProjectUsecase = Depends(project_usecase),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    obj_in = project_in.to_entity()
    project = ucase.create(user_id=current_user.id, obj_in=obj_in)
    project = schemas.ProjectBase(**asdict(project))
    project_schema_reponse = schemas.ProjectCreateReponse(
        status = 200,
        message="success",
        data=project
    )
    return project_schema_reponse

@router.get("/{project_id}")
def get_project_by_id(
    project_id: str,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    ucase: usecase.ProjectUsecase = Depends(project_usecase),
):
    project = ucase.get_project_by_id(project_id=project_id)
    project = schemas.ProjectBase(**asdict(project))
    project_schema_reponse = schemas.ProjectResponse(
        status=200,
        message="success",
        data=project
    )
    return project_schema_reponse


@router.get("/")
def read_projects(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    ucase: usecase.ProjectUsecase = Depends(project_usecase),
):
    try:
        projects = ucase.get_multi(skip=skip, limit=limit, user_id=current_user.id)
    except exceptions.RepositoryException as e:
        raise HTTPException(status_code=400, detail=e.message)
    
    response = schemas.ListProjectResponse(
        **asdict(projects),
    )
    return response


@router.put("/{project_id}")
def update_project(
    *,
    db: Session = Depends(deps.get_db),
    project_id: str,
    project_in: schemas.ProjectUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
    ucase: usecase.ProjectUsecase = Depends(project_usecase),
):
    project_in = project_in.to_entity()
    project = ucase.update(id=uuid.UUID(project_id), obj_in=project_in)
    project = schemas.ProjectInDB(**asdict(project))
    project_schema_reponse = schemas.ProjectUpdateReponse(
        status=200,
        message="success",
        data=project
    )
    return project_schema_reponse