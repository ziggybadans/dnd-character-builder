"""Common test fixtures and configuration."""

import asyncio
from typing import AsyncGenerator, Generator

import pytest
import pytest_asyncio
from app.database import Base, async_session, engine
from app.main import app
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture(scope="session")
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def test_app() -> FastAPI:
    """Create a test instance of the FastAPI application."""
    return app


@pytest.fixture(scope="session")
def client(test_app: FastAPI) -> Generator[TestClient, None, None]:
    """Create a test client for the FastAPI application."""
    with TestClient(test_app) as test_client:
        yield test_client


@pytest_asyncio.fixture(scope="function")
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """Create a fresh database session for a test."""
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
        async with async_session() as session:
            yield session
            await session.rollback()
        await connection.run_sync(Base.metadata.drop_all)


@pytest.fixture(autouse=True)
def _setup_logging(monkeypatch):
    """Configure logging for tests."""
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")
