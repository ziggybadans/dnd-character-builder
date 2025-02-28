"""Unit tests for the base model."""

from datetime import datetime

import pytest
from app.models.base import BaseModel
from sqlalchemy import Column, String


class TestModel(BaseModel):
    """Test model for testing BaseModel functionality."""

    name = Column(String(50))


def test_base_model_tablename() -> None:
    """Test that the tablename is generated correctly from the class name."""
    assert TestModel.__tablename__ == "testmodel"


def test_base_model_to_dict() -> None:
    """Test that to_dict converts model instance to dictionary."""
    # Create a test model instance
    model = TestModel(name="Test")
    model.id = 1
    model.created_at = datetime(2023, 1, 1, 12, 0, 0)
    model.updated_at = datetime(2023, 1, 1, 12, 0, 0)

    # Convert to dictionary
    model_dict = model.to_dict()

    # Check dictionary values
    assert model_dict["id"] == 1
    assert model_dict["name"] == "Test"
    assert model_dict["created_at"] == datetime(2023, 1, 1, 12, 0, 0)
    assert model_dict["updated_at"] == datetime(2023, 1, 1, 12, 0, 0)
