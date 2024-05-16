import pytest
from typing import Generator
from src.fastapi_todos.dbase.session import SessionLocal
from src.fastapi_todos.main import create_application
from starlette.testclient import TestClient

@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    application = create_application()
    with TestClient(application) as c:
        yield c