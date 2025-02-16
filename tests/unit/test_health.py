"""Unit tests for the health endpoint."""

import pytest
from app.main import app
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""
    return TestClient(app)


def test_health_check_returns_200(client):
    """Test that the health check endpoint returns a 200 status code."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_check_returns_correct_content_type(client):
    """Test that the health check endpoint returns JSON content type."""
    response = client.get("/health")
    assert response.headers["content-type"] == "application/json"


def test_health_check_returns_correct_cors_headers(client):
    """Test that the health check endpoint returns correct CORS headers."""
    response = client.get("/health")
    assert "access-control-allow-origin" in response.headers
    assert response.headers["access-control-allow-origin"] == "http://localhost:3000"
