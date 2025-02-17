"""Pydantic schemas for the D&D Character Builder."""

from .background import Background, BackgroundBase, BackgroundCreate
from .base import BaseInDB, BaseSchema, NameDescriptionBase
from .character import Character, CharacterBase, CharacterCreate, CharacterUpdate
from .class_ import Class, ClassBase, ClassCreate, Subclass, SubclassBase, SubclassCreate
from .race import Race, RaceBase, RaceCreate, Subrace, SubraceBase, SubraceCreate

__all__ = [
    # Base schemas
    "BaseSchema",
    "BaseInDB",
    "NameDescriptionBase",
    # Race schemas
    "Race",
    "RaceCreate",
    "RaceBase",
    "Subrace",
    "SubraceCreate",
    "SubraceBase",
    # Class schemas
    "Class",
    "ClassCreate",
    "ClassBase",
    "Subclass",
    "SubclassCreate",
    "SubclassBase",
    # Background schemas
    "Background",
    "BackgroundCreate",
    "BackgroundBase",
    # Character schemas
    "Character",
    "CharacterCreate",
    "CharacterUpdate",
    "CharacterBase",
]
