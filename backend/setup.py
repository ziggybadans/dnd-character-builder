"""Setup file for the D&D Character Builder backend."""

from setuptools import find_packages, setup

setup(
    name="dnd-character-builder",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.104.0",
        "uvicorn>=0.34.0",
        "sqlalchemy>=2.0.0",
        "alembic>=1.12.0",
        "pydantic>=2.10.0",
        "python-jose>=3.3.0",
        "passlib>=1.7.4",
        "python-multipart>=0.0.18",
        "pytest>=7.4.3",
        "pytest-asyncio>=0.21.1",
        "coverage>=7.6.12",
    ],
)
