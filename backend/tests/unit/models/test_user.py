"""Unit tests for user model."""

import pytest
from app.models.user import User


def test_user_creation() -> None:
    """Test creating a user."""
    user = User(
        username="testuser",
        email="test@example.com",
        hashed_password="hashedpassword123",
        is_active=True,
        is_superuser=False,
    )

    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.hashed_password == "hashedpassword123"
    assert user.is_active is True
    assert user.is_superuser is False
    assert user.characters == []


def test_user_repr() -> None:
    """Test the string representation of a user."""
    user = User(username="admin", email="admin@example.com", hashed_password="adminpassword123")

    assert repr(user) == "<User admin>"
