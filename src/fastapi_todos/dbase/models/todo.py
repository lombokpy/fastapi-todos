import uuid

from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from dbase.base_class import Base
from todo import domain


class Todo(Base):
    __tablename__ = "todos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)
    project = relationship("Project", backref="todos")

    def to_entity(self) -> domain.Todo:
        return domain.Todo(
        id=uuid.UUID(str(self.id)),
        title=self.title,
        description=self.description,
        is_completed=self.is_completed,
        created_at=self.created_at,
        updated_at=self.updated_at,
        project_id=uuid.UUID(str(self.project_id)),
        )