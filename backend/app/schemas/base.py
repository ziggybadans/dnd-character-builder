"""Base Pydantic models for the D&D Character Builder."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """Base schema with common configuration."""

    model_config = ConfigDict(from_attributes=True)


class NameDescriptionBase(BaseSchema):
    """Base schema for models with name and description."""

    name: str
    description: str


class BaseInDB(NameDescriptionBase):
    """Base schema for database models."""

    id: int
    created_at: datetime
    updated_at: datetime
