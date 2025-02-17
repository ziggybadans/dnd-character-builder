"""Unit tests for error handlers module."""

from typing import Any, Callable

import pytest
from app.utils.error_handlers import (
    generic_exception_handler,
    sqlalchemy_exception_handler,
    validation_exception_handler,
)
from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, Field, ValidationError
from pytest import MarkDecorator
from sqlalchemy.exc import SQLAlchemyError


def typed_async_test(func: Callable[..., Any]) -> Any:
    """Type-aware decorator for async test functions."""
    mark_asyncio: MarkDecorator = pytest.mark.asyncio
    return mark_asyncio(func)


@typed_async_test
async def test_validation_exception_handler() -> None:
    """Test handling of validation errors."""

    class TestModel(BaseModel):
        """Test model for validation errors."""

        name: str = Field(..., min_length=3)

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


@typed_async_test
async def test_sqlalchemy_exception_handler() -> None:
    """Test handling of SQLAlchemy errors."""
    request = Request({"type": "http", "method": "GET", "url": "http://test"})
    exc = SQLAlchemyError("Test database error")
    response = await sqlalchemy_exception_handler(request, exc)

    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    content = response.body.decode()
    assert "Database error occurred" in content
    assert "Test database error" in content


@typed_async_test
async def test_generic_exception_handler() -> None:
    """Test handling of generic exceptions."""
    request = Request({"type": "http", "method": "GET", "url": "http://test"})
    exc = Exception("Test generic error")
    response = await generic_exception_handler(request, exc)

    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    content = response.body.decode()
    assert "An unexpected error occurred" in content
    assert "Test generic error" in content
