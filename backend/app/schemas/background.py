"""Pydantic models for backgrounds."""

from typing import Dict, List

from .base import BaseInDB, BaseSchema, NameDescriptionBase


class BackgroundBase(NameDescriptionBase):
    """Base schema for backgrounds."""

    proficiencies: Dict[str, List[str] | Dict[str, int]]
    equipment: List[str]
    feature: Dict[str, str]
    characteristics: Dict[str, List[str]]
    source_book: str


class BackgroundCreate(BackgroundBase):
    """Schema for creating a background."""

    pass


class Background(BackgroundBase, BaseInDB):
    """Schema for a background in the database."""

    pass
