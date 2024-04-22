import uuid

from sqlalchemy import Column, String, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from dbase.base_class import Base
from project import domain


class Project(Base):
    __tablename__ = "projects"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    user = relationship("User", backref="projects")

    def to_entity(self) -> domain.Project:
        return domain.Project(
            id=uuid.UUID(str(self.id)),
            user_id=uuid.UUID(str(self.user_id)),
            name=self.name,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )