"""Unit tests for Pydantic schemas."""

from datetime import datetime

import pytest
from app.schemas import (
    Background,
    BackgroundCreate,
    Character,
    CharacterCreate,
    CharacterUpdate,
    Class,
    ClassCreate,
    Race,
    RaceCreate,
    Subclass,
    SubclassCreate,
    Subrace,
    SubraceCreate,
)
from pydantic import ValidationError


def test_race_schema_validation(sample_race_data):
    """Test race schema validation."""
    # Test successful validation
    race_create = RaceCreate(**sample_race_data)
    assert race_create.name == sample_race_data["name"]
    assert race_create.ability_score_increase == sample_race_data["ability_score_increase"]

    # Test invalid ability score
    invalid_data = sample_race_data.copy()
    invalid_data["ability_score_increase"] = {"invalid": "value"}
    with pytest.raises(ValidationError):
        RaceCreate(**invalid_data)


def test_subrace_schema_validation(sample_subrace_data):
    """Test subrace schema validation."""
    # Test successful validation
    subrace_data = sample_subrace_data.copy()
    subrace_data["race_id"] = 1
    subrace_create = SubraceCreate(**subrace_data)
    assert subrace_create.name == sample_subrace_data["name"]
    assert subrace_create.race_id == 1

    # Test missing race_id
    with pytest.raises(ValidationError):
        SubraceCreate(**sample_subrace_data)


def test_class_schema_validation(sample_class_data):
    """Test class schema validation."""
    # Test successful validation
    class_create = ClassCreate(**sample_class_data)
    assert class_create.name == sample_class_data["name"]
    assert class_create.hit_die == sample_class_data["hit_die"]

    # Test invalid hit die
    invalid_data = sample_class_data.copy()
    invalid_data["hit_die"] = "invalid"
    with pytest.raises(ValidationError):
        ClassCreate(**invalid_data)


def test_subclass_schema_validation(sample_subclass_data):
    """Test subclass schema validation."""
    # Test successful validation
    subclass_data = sample_subclass_data.copy()
    subclass_data["class_id"] = 1
    subclass_create = SubclassCreate(**subclass_data)
    assert subclass_create.name == sample_subclass_data["name"]
    assert subclass_create.class_id == 1

    # Test missing class_id
    with pytest.raises(ValidationError):
        SubclassCreate(**sample_subclass_data)


def test_background_schema_validation(sample_background_data):
    """Test background schema validation."""
    # Test successful validation
    background_create = BackgroundCreate(**sample_background_data)
    assert background_create.name == sample_background_data["name"]
    assert background_create.equipment == sample_background_data["equipment"]

    # Test invalid equipment format
    invalid_data = sample_background_data.copy()
    invalid_data["equipment"] = {"invalid": "format"}
    with pytest.raises(ValidationError):
        BackgroundCreate(**invalid_data)


def test_character_schema_validation(sample_character_data):
    """Test character schema validation."""
    # Test successful validation
    character_data = sample_character_data.copy()
    character_data.update({"race_id": 1, "class_id": 1, "background_id": 1})
    character_create = CharacterCreate(**character_data)
    assert character_create.name == sample_character_data["name"]
    assert character_create.level == sample_character_data["level"]

    # Test invalid ability score
    invalid_data = character_data.copy()
    invalid_data["strength"] = 25  # Above maximum
    with pytest.raises(ValidationError):
        CharacterCreate(**invalid_data)

    # Test invalid level
    invalid_data = character_data.copy()
    invalid_data["level"] = 0  # Below minimum
    with pytest.raises(ValidationError):
        CharacterCreate(**invalid_data)

    # Test hit points validation
    invalid_data = character_data.copy()
    invalid_data["hit_points"] = 10
    invalid_data["max_hit_points"] = 12
    with pytest.raises(ValidationError):
        CharacterCreate(**invalid_data)


def test_character_update_schema():
    """Test character update schema validation."""
    # Test partial update
    update_data = {"hit_points": 10, "temporary_hit_points": 5}
    character_update = CharacterUpdate(**update_data)
    assert character_update.hit_points == update_data["hit_points"]
    assert character_update.temporary_hit_points == update_data["temporary_hit_points"]

    # Test invalid update
    invalid_data = {"hit_points": -1}  # Below minimum
    with pytest.raises(ValidationError):
        CharacterUpdate(**invalid_data)


def test_schema_relationships(
    sample_race_data,
    sample_subrace_data,
    sample_class_data,
    sample_subclass_data,
    sample_background_data,
    sample_character_data,
):
    """Test schema relationships and nested models."""
    # Create base models
    race = Race(
        **sample_race_data, id=1, created_at=datetime.now(), updated_at=datetime.now(), subraces=[]
    )

    class_ = Class(
        **sample_class_data,
        id=1,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        subclasses=[],
    )

    background = Background(
        **sample_background_data, id=1, created_at=datetime.now(), updated_at=datetime.now()
    )

    # Create character with relationships
    character_data = sample_character_data.copy()
    character_data.update(
        {
            "id": 1,
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
            "race_id": race.id,
            "class_id": class_.id,
            "background_id": background.id,
            "race": race,
            "character_class": class_,
            "background": background,
        }
    )

    character = Character(**character_data)
    assert character.race.name == sample_race_data["name"]
    assert character.character_class.name == sample_class_data["name"]
    assert character.background.name == sample_background_data["name"]
