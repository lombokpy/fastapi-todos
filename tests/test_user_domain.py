import pytest
from datetime import datetime
from uuid import UUID
from user.domain import User  # Import your User class

@pytest.fixture
def user_data():
    return {
        'id': UUID('123e4567-e89b-12d3-a456-426614174000'),
        'full_name': 'John Doe',
        'email': 'john@example.com',
        'hashed_password': 'hashedpassword',
        'password': 'password',
        'is_active': True,
        'is_superuser': False,
        'created_at': datetime.now(),
        'updated_at': datetime.now()
    }

def test_user_creation(user_data):
    # Act
    user = User(**user_data)

    # Assert
    assert user.id == user_data['id']
    assert user.full_name == user_data['full_name']
    assert user.email == user_data['email']
    assert user.hashed_password == user_data['hashed_password']
    assert user.password == user_data['password']
    assert user.is_active == user_data['is_active']
    assert user.is_superuser == user_data['is_superuser']
    assert user.created_at == user_data['created_at']
    assert user.updated_at == user_data['updated_at']
