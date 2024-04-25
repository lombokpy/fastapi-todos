from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core import deps
from todo import usecase, repository, schemas
from typing import Any
from dbase import models
from dataclasses import asdict
import uuid
from shared import exceptions

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