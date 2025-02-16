import os
from functools import lru_cache
from pathlib import Path

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings managed through environment variables."""

    # Project base directory
    BASE_DIR: Path = Path(__file__).resolve().parent.parent

    # Database
    DATABASE_URL: str = f"sqlite:///{BASE_DIR}/data/dnd_character_builder.db"

    # Security
    SECRET_KEY: str = "development_secret_key"  # Change in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "D&D Character Builder"

    # CORS
    BACKEND_CORS_ORIGINS: list[str] = [
        "http://localhost:5173",  # Frontend development server
        "http://localhost:8000",  # Backend development server
    ]

    model_config = ConfigDict(case_sensitive=True, env_file=".env")


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
