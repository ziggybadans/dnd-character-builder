"""Unit tests for error handlers module."""
import pytest
from app.utils.error_handlers import (
    generic_exception_handler,
    sqlalchemy_exception_handler,
    validation_exception_handler,
)
from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, Field, ValidationError
from sqlalchemy.exc import SQLAlchemyError


class TestModel(BaseModel):
    """Test model for validation errors."""

    name: str = Field(..., min_length=3)


@pytest.mark.asyncio
async def test_validation_exception_handler():
    """Test handling of validation errors."""
    request = Request({"type": "http", "method": "GET", "url": "http://test"})

    # Create a validation error from raw data
    raw_data = {"name": "a"}  # Invalid data
    try:
        TestModel.model_validate(raw_data)
        pytest.fail("Validation should have failed")
    except ValidationError as e:
        # Convert pydantic ValidationError to FastAPI RequestValidationError
        exc = RequestValidationError(e.errors())
        response = await validation_exception_handler(request, exc)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        content = response.body.decode()
        assert "Validation error in request data" in content
        assert "detail" in content


@pytest.mark.asyncio
async def test_sqlalchemy_exception_handler():
    """Test handling of database errors."""
    request = Request({"type": "http", "method": "GET", "url": "http://test"})
    exc = SQLAlchemyError("Database connection failed")
    response = await sqlalchemy_exception_handler(request, exc)

    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    content = response.body.decode()
    assert "Database error occurred" in content
    assert "Database connection failed" in content


@pytest.mark.asyncio
async def test_generic_exception_handler():
    """Test handling of generic exceptions."""
    request = Request({"type": "http", "method": "GET", "url": "http://test"})
    exc = Exception("Unexpected error")
    response = await generic_exception_handler(request, exc)

    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    content = response.body.decode()
    assert "An unexpected error occurred" in content
    assert "Unexpected error" in content
