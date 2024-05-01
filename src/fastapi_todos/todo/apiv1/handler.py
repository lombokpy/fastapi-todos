from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core import deps
from todo import usecase, repository, schemas
from typing import Any
from dbase import models
from dataclasses import asdict
import uuid

router = APIRouter()


def todo_usecase(session: Session = Depends(deps.get_db)):
    repo = repository.TodoRepository(session)
    ucase = usecase.TodoUsecase(repo)
    return ucase

@router.post("/")
def create_todo(
    todo_in: schemas.TodoCreate,
    project_id: str,
    ucase: usecase.TodoUsecase = Depends(todo_usecase),
    current_user: models.User = Depends(deps.get_current_active_user),
):
    obj_in = todo_in.to_entity()
    todo = ucase.create_todo(obj_in=obj_in, project_id=project_id)
    todo = schemas.TodoInDb(**asdict(todo))
    todo_schema_reponse = schemas.TodoCreateResponse(
        status=200,
        message="success",
        data=todo
    )
    return todo_schema_reponse

@router.get("/{todo_id}")
def get_todo_by_id(
    todo_id: str,
    current_user: models.User = Depends(deps.get_current_active_user),
    ucase: usecase.TodoUsecase = Depends(todo_usecase)
):
    try:
        todo = ucase.get_todo(id=todo_id)
        todo = schemas.TodoInDb(**asdict(todo))
        todo_schema_reponse = schemas.TodoGetResponse(
            status=status.HTTP_200_OK,
            message="success",
            data=todo
        )
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="data is not found")
    return todo_schema_reponse

@router.get("/")
def read_todos(
    project_id: str,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    ucase: usecase.TodoUsecase = Depends(todo_usecase)
):
    todos = ucase.get_multi(skip=skip, limit=limit, project_id=project_id)
    response = schemas.TodoListResponse(
        **asdict(todos),
    )
    return response


@router.put("/{todo_id}")
def update_todo(
    todo_id: str,
    todo_in: schemas.TodoUpdate,
    ucase: usecase.TodoUsecase = Depends(todo_usecase),
    current_user: models.User = Depends(deps.get_current_active_user),
):
    todo_in = todo_in.to_entity()
    todo = ucase.update_todo(id=todo_id, obj_in=todo_in)
    data = schemas.TodoInDb(**asdict(todo))
    response = schemas.TodoUpdateResponse(
        status=status.HTTP_200_OK,
        message="Todo was updated",
        data=data
    )
    return response

@router.put("/{todo_id}/done")
def todo_done(
    todo_id: str,
    todo_in: schemas.TodoDoneRequest,
    ucase: usecase.TodoUsecase = Depends(todo_usecase),
    current_user: models.User = Depends(deps.get_current_active_user),
):
    todo_in = todo_in.to_entity()
    todo = ucase.done(id=todo_id, obj_in=todo_in)
    todo = schemas.TodoInDb(**asdict(todo))
    response = schemas.TodoDoneReponse(
        status = status.HTTP_202_ACCEPTED,
        message="Todo item successfully marked as completed.",
        data=todo
    )
    return response

@router.put("/{todo_id}/start")
def todo_timer_start(
    todo_id: str,
    todo_in: schemas.TodoStartedAtRequest,
    ucase: usecase.TodoUsecase = Depends(todo_usecase),
    current_user: models.User = Depends(deps.get_current_active_user),
):
    todo_in = todo_in.to_entity()
    todo = ucase.start_timer(id=todo_id, obj_in=todo_in)
    todo = schemas.TodoInDb(**asdict(todo))
    response = schemas.TodoStartedAtReponse(
        status=status.HTTP_202_ACCEPTED,
        message="Timer successfully started",
        data=todo
    )
    return response

@router.put("/{todo_id}/stop")
def todo_timer_stop(
    todo_id: str,
    todo_in: schemas.TodoEndedAtRequest,
    ucase: usecase.TodoUsecase = Depends(todo_usecase),
    current_user: models.User = Depends(deps.get_current_active_user),
):
    todo_in = todo_in.to_entity()
    todo = ucase.stop_timer(id=todo_id, obj_in=todo_in)
    todo = schemas.TodoInDb(**asdict(todo))
    response = schemas.TodoEndedAtReponse(
        status=status.HTTP_202_ACCEPTED,
        message="Timer successfully stopped",
        data=todo
    )
    return response

@router.delete("/{todo_id}")
def delete_todo(
    todo_id: str,
    ucase: usecase.TodoUsecase = Depends(todo_usecase),
    current_user: models.User = Depends(deps.get_current_active_user),
):
    ucase.delete_todo(id=todo_id)
    response = schemas.TodoDeleteResponse(
        status=status.HTTP_200_OK,
        message="Todo was deleted",
        data=None
    )
    return response