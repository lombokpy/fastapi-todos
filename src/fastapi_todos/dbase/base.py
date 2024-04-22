# Import all the models, so that Base has them before being
# imported by Alembic
from dbase.base_class import Base  # noqa
from dbase.models.user import User  # noqa
from dbase.models.project import Project #noqa