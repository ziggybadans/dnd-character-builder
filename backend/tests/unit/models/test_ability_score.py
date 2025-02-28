"""Unit tests for ability score models."""

import pytest
from app.models.ability_score import AbilityScore, CharacterAbilityScore
from app.models.character import Character
from sqlalchemy.orm import Session


def test_ability_score_creation() -> None:
    """Test creating an ability score."""
    ability = AbilityScore(
        name="Strength", abbreviation="STR", description="Measures physical power"
    )

    assert ability.name == "Strength"
    assert ability.abbreviation == "STR"
    assert ability.description == "Measures physical power"
    assert ability.character_ability_scores == []


def test_ability_score_repr() -> None:
    """Test the string representation of an ability score."""
    ability = AbilityScore(name="Dexterity", abbreviation="DEX", description="Measures agility")

    assert repr(ability) == "<AbilityScore Dexterity>"


def test_character_ability_score_total_value() -> None:
    """Test calculating the total ability score value."""
    char_ability = CharacterAbilityScore(base_value=15, racial_bonus=2, asi_bonus=1, misc_bonus=1)

    assert char_ability.total_value == 19


def test_character_ability_score_modifier() -> None:
    """Test calculating the ability score modifier."""
    # Test various ability scores and their expected modifiers
    test_cases = [
        (1, -5),  # 1 -> -5
        (2, -4),  # 2 -> -4
        (3, -4),  # 3 -> -4
        (4, -3),  # 4 -> -3
        (8, -1),  # 8 -> -1
        (9, -1),  # 9 -> -1
        (10, 0),  # 10 -> 0
        (11, 0),  # 11 -> 0
        (12, 1),  # 12 -> 1
        (15, 2),  # 15 -> 2
        (18, 4),  # 18 -> 4
        (20, 5),  # 20 -> 5
        (24, 7),  # 24 -> 7
        (30, 10),  # 30 -> 10
    ]

    for score, expected_modifier in test_cases:
        # Initialize with default values for bonuses to avoid None
        char_ability = CharacterAbilityScore(
            base_value=score, racial_bonus=0, asi_bonus=0, misc_bonus=0
        )
        assert (
            char_ability.modifier == expected_modifier
        ), f"Score {score} should have modifier {expected_modifier}"


def test_character_ability_score_repr() -> None:
    """Test the string representation of a character ability score."""
    ability = AbilityScore(name="Wisdom", abbreviation="WIS", description="Measures perception")
    char_ability = CharacterAbilityScore(
        character_id=1, ability_score_id=1, base_value=14, ability_score=ability
    )

    assert repr(char_ability) == "<CharacterAbilityScore 1:Wisdom>"

    # Test without ability score
    char_ability2 = CharacterAbilityScore(character_id=2, ability_score_id=2, base_value=12)
    assert repr(char_ability2) == "<CharacterAbilityScore 2:Unknown>"
