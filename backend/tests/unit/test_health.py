"""Unit tests for health check endpoint."""

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_health_check() -> None:
    """Test the health check endpoint.

    Verifies that the health check endpoint returns a 200 status code
    and the correct response format.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "message": "API is running"}
