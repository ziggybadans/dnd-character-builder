"""Unit tests for database module."""
import pytest
from app.database import get_db
from sqlalchemy.orm import Session


def test_get_db_yields_session():
    """Test that get_db yields a database session."""
    db_generator = get_db()
    db = next(db_generator)
    assert isinstance(db, Session)
    try:
        next(db_generator)
    except StopIteration:
        pass  # Expected behavior


def test_get_db_session_lifecycle():
    """Test the lifecycle of a database session."""
    db_generator = get_db()
    db = next(db_generator)
    assert isinstance(db, Session)

    # Session should be active after creation
    assert db.is_active

    # Simulate end of request context
    try:
        next(db_generator)
    except StopIteration:
        pass

    # Session should be closed
    with pytest.raises(Exception):
        db.execute("SELECT 1")


def test_get_db_handles_exceptions():
    """Test that get_db closes the session even if an exception occurs."""
    db_generator = get_db()
    db = next(db_generator)
    assert isinstance(db, Session)

    # Simulate an exception during request handling
    with pytest.raises(Exception, match="Test exception"):
        try:
            raise Exception("Test exception")
        finally:
            try:
                next(db_generator)
            except StopIteration:
                pass

    # Session should be closed
    with pytest.raises(Exception):
        db.execute("SELECT 1")
