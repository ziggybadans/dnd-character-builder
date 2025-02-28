"""Unit tests for character model."""

import pytest
from app.models.background import Background
from app.models.character import Alignment, Character
from app.models.race import Race, Subrace


def test_character_creation() -> None:
    """Test creating a character."""
    race = Race(
        name="Human",
        description="Humans are the most adaptable and ambitious people among the common races",
    )

    subrace = Subrace(
        name="Variant Human",
        description="Variant humans have more customization options",
        race=race,
    )

    background = Background(
        name="Soldier", description="You have been trained as a soldier and fought in a war"
    )

    character = Character(
        name="Aragorn",
        level=5,
        experience_points=6500,
        alignment=Alignment.LAWFUL_GOOD,
        age=30,
        height="6'2\"",
        weight="185 lbs",
        eyes="Gray",
        skin="Fair",
        hair="Dark Brown",
        personality_traits="I'm always polite and respectful.",
        ideals="The greater good. Our lot is to lay down our lives in defense of others.",
        bonds="I fight for those who cannot fight for themselves.",
        flaws="I have a weakness for the vices of the city, especially fine food and wine.",
        backstory="Aragorn was raised by elves after his father died...",
        max_hit_points=45,
        current_hit_points=45,
        temporary_hit_points=0,
        armor_class=16,
        initiative=2,
        speed=30,
        inspiration=False,
        death_saves_successes=0,
        death_saves_failures=0,
        race_id=1,
        subrace_id=1,
        background_id=1,
        race=race,
        subrace=subrace,
        background=background,
    )

    assert character.name == "Aragorn"
    assert character.level == 5
    assert character.experience_points == 6500
    assert character.alignment == Alignment.LAWFUL_GOOD
    assert character.age == 30
    assert character.height == "6'2\""
    assert character.weight == "185 lbs"
    assert character.eyes == "Gray"
    assert character.skin == "Fair"
    assert character.hair == "Dark Brown"
    assert character.personality_traits == "I'm always polite and respectful."
    assert (
        character.ideals
        == "The greater good. Our lot is to lay down our lives in defense of others."
    )
    assert character.bonds == "I fight for those who cannot fight for themselves."
    assert (
        character.flaws
        == "I have a weakness for the vices of the city, especially fine food and wine."
    )
    assert character.backstory == "Aragorn was raised by elves after his father died..."
    assert character.max_hit_points == 45
    assert character.current_hit_points == 45
    assert character.temporary_hit_points == 0
    assert character.armor_class == 16
    assert character.initiative == 2
    assert character.speed == 30
    assert character.inspiration is False
    assert character.death_saves_successes == 0
    assert character.death_saves_failures == 0
    assert character.race_id == 1
    assert character.subrace_id == 1
    assert character.background_id == 1
    assert character.race.name == "Human"
    assert character.subrace.name == "Variant Human"
    assert character.background.name == "Soldier"
    assert character.class_levels == []
    assert character.ability_scores == []
    assert character.skills == []
    assert character.proficiencies == []


def test_character_repr() -> None:
    """Test the string representation of a character."""
    character = Character(name="Gandalf", level=10)

    assert repr(character) == "<Character Gandalf (Level 10)>"


def test_character_proficiency_bonus() -> None:
    """Test calculating the proficiency bonus based on character level."""
    # Test various levels and their expected proficiency bonuses
    test_cases = [
        (1, 2),  # Level 1 -> +2
        (2, 2),  # Level 2 -> +2
        (3, 2),  # Level 3 -> +2
        (4, 2),  # Level 4 -> +2
        (5, 3),  # Level 5 -> +3
        (6, 3),  # Level 6 -> +3
        (7, 3),  # Level 7 -> +3
        (8, 3),  # Level 8 -> +3
        (9, 4),  # Level 9 -> +4
        (10, 4),  # Level 10 -> +4
        (11, 4),  # Level 11 -> +4
        (12, 4),  # Level 12 -> +4
        (13, 5),  # Level 13 -> +5
        (17, 6),  # Level 17 -> +6
        (20, 6),  # Level 20 -> +6
    ]

    for level, expected_bonus in test_cases:
        character = Character(name="Test", level=level)
        assert (
            character.proficiency_bonus == expected_bonus
        ), f"Level {level} should have proficiency bonus +{expected_bonus}"
