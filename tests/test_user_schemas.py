import pytest
from user.schemas import UserBase  # Import your User class
from pydantic import EmailStr

@pytest.fixture
def user_base_data():
    return {
        'email': 'john@example.com',
        'is_active': True,
        'is_superuser': False,
        'full_name': 'John Doe',
    }

def test_user_base_to_entity(user_base_data):
    # Arrange
    user_base: UserBase = UserBase(**user_base_data)

    # Act
    user_entity = user_base.to_entity()

    # Assert
    assert user_entity.email == user_base.email
    assert user_entity.full_name == user_base.full_name
    assert user_entity.is_active == user_base.is_active
    assert user_entity.is_superuser == user_base.is_superuser

def test_user_base_to_entity_no_full_name():
    # Arrange
    user_base_data = {
        'email': 'john@example.com',
        'is_active': True,
        'is_superuser': False
    }
    user_base = UserBase(**user_base_data)

    # Act
    user_entity = user_base.to_entity()

    # Assert
    assert user_entity.email == user_base.email
    assert user_entity.full_name == ""
    assert user_entity.is_active == user_base.is_active
    assert user_entity.is_superuser == user_base.is_superuser
