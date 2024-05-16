import uuid
import pytest
from user.repository import UserV2Repository
from user import domain

@pytest.fixture
def repo_user(db):
    r_user = UserV2Repository(db)
    return r_user


def test_get_user(repo_user) -> domain.User:
    id = uuid.UUID("1a90dcdc-72a2-4e5d-98c6-76d8b39f2dec")
    user = repo_user.get(id)
    assert user is not None


def test_count_user(repo_user) -> int:
    user = repo_user.count()
    assert user is not None
    assert type(user) is int


def test_get_user_by_email(repo_user) -> domain.User:
    m_email = "manolo@gmail.com"
    user = repo_user.get_by_email(email=m_email)
    assert user is not None
    assert user.email == m_email
