"""Pydantic models for classes and subclasses."""

from typing import Dict, List, Optional

from pydantic import Field, field_validator

from .base import BaseInDB, BaseSchema, NameDescriptionBase


class SubclassBase(NameDescriptionBase):
    """Base schema for subclasses."""

    features_by_level: Dict[str, List[Dict[str, str]]]
    spellcasting_ability: Optional[str] = None
    source_book: str


class SubclassCreate(SubclassBase):
    """Schema for creating a subclass."""

    class_id: int


class Subclass(SubclassBase, BaseInDB):
    """Schema for a subclass in the database."""

    class_id: int


class ClassBase(NameDescriptionBase):
    """Base schema for classes."""

    hit_die: str = Field(pattern=r"^d(4|6|8|10|12|20)$")
    primary_ability: List[str]
    saving_throws: List[str]
    proficiencies: Dict[str, List[str] | Dict[str, int | List[str]]]
    starting_equipment: Dict[str, List[List[str]]]
    spellcasting_ability: Optional[str] = None
    spell_slots_progression: Optional[Dict[str, Dict[str, int]]] = None
    features_by_level: Dict[str, List[Dict[str, str]]]
    source_book: str

    @field_validator("primary_ability", "saving_throws")
    def validate_abilities(cls, v: List[str]) -> List[str]:
        """Validate ability scores."""
        valid_abilities = {
            "strength",
            "dexterity",
            "constitution",
            "intelligence",
            "wisdom",
            "charisma",
        }
        for ability in v:
            if ability.lower() not in valid_abilities:
                raise ValueError(f"Invalid ability: {ability}")
        return v


class ClassCreate(ClassBase):
    """Schema for creating a class."""

    pass


class Class(ClassBase, BaseInDB):
    """Schema for a class in the database."""

    subclasses: List[Subclass] = Field(default_factory=list)
