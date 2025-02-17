"""Pydantic models for characters."""

from typing import Dict, List, Optional

from pydantic import Field, field_validator, model_validator

from .background import Background
from .base import BaseInDB, BaseSchema, NameDescriptionBase
from .class_ import Class, Subclass
from .race import Race, Subrace


class CharacterBase(NameDescriptionBase):
    """Base schema for characters."""

    level: int = Field(default=1, ge=1, le=20)
    experience_points: int = Field(default=0, ge=0)
    alignment: str = Field(pattern=r"^(Lawful|Neutral|Chaotic) (Good|Neutral|Evil)$|^True Neutral$")

    # Ability Scores
    strength: int = Field(ge=1, le=20)
    dexterity: int = Field(ge=1, le=20)
    constitution: int = Field(ge=1, le=20)
    intelligence: int = Field(ge=1, le=20)
    wisdom: int = Field(ge=1, le=20)
    charisma: int = Field(ge=1, le=20)

    # Character Stats
    hit_points: int = Field(ge=1)
    max_hit_points: int = Field(ge=1)
    temporary_hit_points: int = Field(default=0, ge=0)
    armor_class: int = Field(ge=1)
    initiative: int
    speed: int = Field(ge=0)

    # Additional Information
    proficiencies: Dict[str, List[str]]
    features: Dict[str, str | bool | int]
    equipment: Dict[str, List[str]]
    spells: Optional[Dict[str, List[str]]] = None
    personality: Dict[str, List[str]]

    @model_validator(mode="after")
    def validate_hit_points(self) -> "CharacterBase":
        """Validate hit points don't exceed max hit points."""
        if self.hit_points > self.max_hit_points:
            raise ValueError("Hit points cannot exceed max hit points")
        return self


class CharacterCreate(CharacterBase):
    """Schema for creating a character."""

    race_id: int
    subrace_id: Optional[int] = None
    class_id: int
    subclass_id: Optional[int] = None
    background_id: int

    @model_validator(mode="after")
    def validate_initial_hit_points(self) -> "CharacterCreate":
        """Validate that hit points equal max hit points on creation."""
        if self.hit_points != self.max_hit_points:
            raise ValueError("Hit points must equal max hit points on character creation")
        return self


class CharacterUpdate(BaseSchema):
    """Schema for updating a character."""

    name: Optional[str] = None
    description: Optional[str] = None
    level: Optional[int] = Field(default=None, ge=1, le=20)
    experience_points: Optional[int] = Field(default=None, ge=0)
    hit_points: Optional[int] = Field(default=None, ge=0)
    temporary_hit_points: Optional[int] = Field(default=None, ge=0)
    armor_class: Optional[int] = Field(default=None, ge=1)
    initiative: Optional[int] = None
    speed: Optional[int] = Field(default=None, ge=0)
    proficiencies: Optional[Dict[str, List[str]]] = None
    features: Optional[Dict[str, str | bool | int]] = None
    equipment: Optional[Dict[str, List[str]]] = None
    spells: Optional[Dict[str, List[str]]] = None
    personality: Optional[Dict[str, List[str]]] = None


class Character(CharacterBase, BaseInDB):
    """Schema for a character in the database."""

    race_id: int
    subrace_id: Optional[int] = None
    class_id: int
    subclass_id: Optional[int] = None
    background_id: int

    # Relationships
    race: Race
    subrace: Optional[Subrace] = None
    character_class: Class
    subclass: Optional[Subclass] = None
    background: Background
