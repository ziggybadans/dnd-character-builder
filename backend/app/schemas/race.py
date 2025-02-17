"""Pydantic models for races and subraces."""

from typing import Dict, List, Optional

from pydantic import Field

from .base import BaseInDB, BaseSchema, NameDescriptionBase


class SubraceBase(NameDescriptionBase):
    """Base schema for subraces."""

    ability_score_increase: Dict[str, int]
    traits: Dict[str, bool | int | str]
    source_book: str


class SubraceCreate(SubraceBase):
    """Schema for creating a subrace."""

    race_id: int


class Subrace(SubraceBase, BaseInDB):
    """Schema for a subrace in the database."""

    race_id: int


class RaceBase(NameDescriptionBase):
    """Base schema for races."""

    ability_score_increase: Dict[str, int]
    age: Dict[str, int]
    size: Dict[str, Dict[str, int | str] | str]
    speed: Dict[str, int]
    languages: Dict[str, List[str]]
    traits: Dict[str, bool | int | str]
    source_book: str


class RaceCreate(RaceBase):
    """Schema for creating a race."""

    pass


class Race(RaceBase, BaseInDB):
    """Schema for a race in the database."""

    subraces: List[Subrace] = Field(default_factory=list)
