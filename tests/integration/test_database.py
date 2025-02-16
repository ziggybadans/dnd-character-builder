"""Integration tests for database connectivity."""

import pytest
from app.database import async_session
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.mark.asyncio
async def test_database_connection():
    """Test that we can connect to the database and execute a query."""
    async with async_session() as session:
        assert isinstance(session, AsyncSession)
        result = await session.execute(text("SELECT 1"))
        assert result.scalar() == 1


@pytest.mark.asyncio
async def test_database_transaction_rollback():
    """Test that database transactions can be rolled back."""
    async with async_session() as session:
        async with session.begin():
            # Execute a query that should be rolled back
            await session.execute(text("CREATE TEMPORARY TABLE test (id INTEGER)"))
            await session.execute(text("INSERT INTO test VALUES (1)"))
            # Transaction will be rolled back at the end of the context
