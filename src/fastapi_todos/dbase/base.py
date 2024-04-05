# Import all the models, so that Base has them before being
# imported by Alembic
from dbase.base_class import Base  # noqa
from dbase.models.file_upload import UploadedFile  # noqa
from dbase.models.user import User  # noqa
