import dataclasses
from typing import List, Optional
from project import domain
from sqlalchemy.orm import Session
from uuid import UUID
from dbase import models
from todo import domain


class TodoRepository(domain.Todo):
    def __init__(self, session: Session):
        self.session = session

    def get(self, *, id: UUID) -> domain.Todo:
        todo: models.Todo = self.session.query(models.Todo).filter(models.Todo.id == id).first()
        if todo is not None:
            return todo.to_entity()
        return todo
    
    def get_multi(self, *, skip: int = 0, limit: int = 0, project_id: UUID) -> List[domain.Todo]:
        project = self.session.query(models.Project).filter(models.Project.id == project_id).first()
        if project is None:
            return None
        todos: models.Todo = self.session.query(models.Todo).filter(
            models.Todo.project_id == project_id
        ).offset(skip).limit(limit).all()
        list_todo = [t.to_entity() for t in todos]
        return list_todo
    
    def count(self, *, project_id: UUID) -> int:
        total = self.session.query(models.Todo).filter(models.Todo.project_id == project_id).count()
        return total
        
    def create(self, *, obj_in: domain.Todo, project_id: UUID) -> domain.Todo:
        db_obj = models.Todo(title=obj_in.title, description=obj_in.description, project_id=project_id)
        self.session.add(db_obj)
        self.session.commit()
        return db_obj.to_entity()
    
    def update(self, *, id: UUID, obj_in: domain.Todo) -> domain.Todo:
        db_obj: models.Todo = self.session.query(models.Todo).filter(models.Todo.id == id).first()
        if not db_obj:
            raise Exception("Todo not found")
        
        for field in dataclasses.fields(obj_in):
            value = getattr(obj_in, field.name)
            if value is not None:
                setattr(db_obj, field.name, value)
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return db_obj.to_entity()
    
    def remove(self, id: UUID) -> domain.Todo:
        db_obj: models.Todo = self.session.query(models.Todo).filter(models.Todo.id == id).first()
        self.session.delete(db_obj)
        self.session.commit()
        return db_obj.to_entity()
    
    def done(self, id: UUID, obj_in: domain.Todo) -> domain.Todo:
        db_obj: models.Todo = self.session.query(models.Todo).filter(models.Todo.id == id).first()
        if not db_obj:
            raise Exception("Todo not found")
        
        for field in dataclasses.fields(obj_in):
            value = getattr(obj_in, field.name)
            if value is not None:
                setattr(db_obj, field.name, value)
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return db_obj.to_entity()
    
    def start(self, id: UUID, obj_in: domain.Todo) -> domain.Todo:
        db_obj: models.Todo = self.session.query(models.Todo).filter(models.Todo.id == id).first()
        if not db_obj:
            raise Exception("Todo not found")
        
        for field in dataclasses.fields(obj_in):
            value = getattr(obj_in, field.name)
            if value is not None:
                setattr(db_obj, field.name, value)
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return db_obj.to_entity()
    
    def stop(self, id: UUID, obj_in: domain.Todo) -> domain.Todo:
        db_obj: models.Todo = self.session.query(models.Todo).filter(models.Todo.id == id).first()
        if not db_obj:
            raise Exception("Todo not found")
        
        for field in dataclasses.fields(obj_in):
            value = getattr(obj_in, field.name)
            if value is not None:
                setattr(db_obj, field.name, value)
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return db_obj.to_entity()