"""Unit tests for the logger utility."""

import logging
from unittest.mock import patch

import pytest
from app.utils.logger import get_logger, setup_logging


def test_setup_logging_sets_log_level():
    """Test that setup_logging sets the correct log level."""
    with patch("logging.getLogger") as mock_get_logger:
        mock_logger = mock_get_logger.return_value
        setup_logging("DEBUG")
        mock_logger.setLevel.assert_called_once_with(logging.DEBUG)


def test_setup_logging_configures_handler():
    """Test that setup_logging configures the handler correctly."""
    with patch("logging.getLogger") as mock_get_logger:
        mock_logger = mock_get_logger.return_value
        setup_logging("INFO")
        assert len(mock_logger.handlers) == 1
        assert isinstance(mock_logger.handlers[0], logging.StreamHandler)


@pytest.mark.parametrize(
    "log_level,expected_level",
    [
        ("DEBUG", logging.DEBUG),
        ("INFO", logging.INFO),
        ("WARNING", logging.WARNING),
        ("ERROR", logging.ERROR),
        ("CRITICAL", logging.CRITICAL),
    ],
)
def test_setup_logging_handles_different_levels(log_level, expected_level):
    """Test that setup_logging handles different log levels correctly."""
    with patch("logging.getLogger") as mock_get_logger:
        mock_logger = mock_get_logger.return_value
        setup_logging(log_level)
        mock_logger.setLevel.assert_called_once_with(expected_level)


def test_get_logger_returns_logger():
    """Test that get_logger returns a logger instance."""
    logger = get_logger(__name__)
    assert isinstance(logger, logging.Logger)
    assert logger.name == __name__


def test_get_logger_returns_same_logger():
    """Test that get_logger returns the same logger for the same name."""
    logger1 = get_logger("test_logger")
    logger2 = get_logger("test_logger")
    assert logger1 is logger2
