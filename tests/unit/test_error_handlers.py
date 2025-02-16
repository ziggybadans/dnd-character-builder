"""Unit tests for error handlers."""

import pytest
from app.utils.error_handlers import http_error_handler
from fastapi import HTTPException, Request
from starlette.responses import JSONResponse


@pytest.fixture
def mock_request():
    """Create a mock request object."""
    return Request({"type": "http", "method": "GET", "headers": []})


def test_http_error_handler_returns_json_response(mock_request):
    """Test that the HTTP error handler returns a JSON response."""
    exc = HTTPException(status_code=404, detail="Not found")
    response = http_error_handler(mock_request, exc)
    assert isinstance(response, JSONResponse)
    assert response.status_code == 404


def test_http_error_handler_includes_error_detail(mock_request):
    """Test that the HTTP error handler includes error details in response."""
    exc = HTTPException(status_code=400, detail="Bad request")
    response = http_error_handler(mock_request, exc)
    assert response.body == b'{"detail":"Bad request"}'


def test_http_error_handler_handles_custom_headers(mock_request):
    """Test that the HTTP error handler handles custom headers."""
    exc = HTTPException(
        status_code=401, detail="Unauthorized", headers={"WWW-Authenticate": "Bearer"}
    )
    response = http_error_handler(mock_request, exc)
    assert response.headers["WWW-Authenticate"] == "Bearer"
