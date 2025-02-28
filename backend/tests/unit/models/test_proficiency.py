"""Unit tests for proficiency models."""

from unittest.mock import PropertyMock, patch

import pytest
from app.models.proficiency import CharacterSkill, Proficiency, ProficiencyLevel, ProficiencyType


def test_proficiency_creation() -> None:
    """Test creating a proficiency."""
    proficiency = Proficiency(
        name="Acrobatics",
        description="Your Dexterity (Acrobatics) check covers your attempt to stay on your feet in a tricky situation.",
        type=ProficiencyType.SKILL,
        ability_score="Dexterity",
    )

    assert proficiency.name == "Acrobatics"
    assert (
        proficiency.description
        == "Your Dexterity (Acrobatics) check covers your attempt to stay on your feet in a tricky situation."
    )
    assert proficiency.type == ProficiencyType.SKILL
    assert proficiency.ability_score == "Dexterity"
    assert proficiency.characters == []
    assert proficiency.races == []
    assert proficiency.backgrounds == []
    assert proficiency.character_classes == []


def test_proficiency_repr() -> None:
    """Test the string representation of a proficiency."""
    proficiency = Proficiency(name="Acrobatics", type=ProficiencyType.SKILL)

    assert "Acrobatics" in repr(proficiency)
    assert "SKILL" in repr(proficiency)


def test_character_skill_creation() -> None:
    """Test creating a character skill."""
    proficiency = Proficiency(
        name="Acrobatics",
        description="Your Dexterity (Acrobatics) check covers your attempt to stay on your feet in a tricky situation.",
        type=ProficiencyType.SKILL,
        ability_score="Dexterity",
    )

    character_skill = CharacterSkill(
        character_id=1,
        proficiency_id=1,
        proficiency_level=ProficiencyLevel.PROFICIENT,
        proficiency=proficiency,
    )

    assert character_skill.character_id == 1
    assert character_skill.proficiency_id == 1
    assert character_skill.proficiency_level == ProficiencyLevel.PROFICIENT
    assert character_skill.proficiency.name == "Acrobatics"


def test_character_skill_repr() -> None:
    """Test the string representation of a character skill."""
    proficiency = Proficiency(
        name="Acrobatics", type=ProficiencyType.SKILL, ability_score="Dexterity"
    )

    character_skill = CharacterSkill(
        character_id=1,
        proficiency_id=1,
        proficiency_level=ProficiencyLevel.PROFICIENT,
        proficiency=proficiency,
    )

    assert "Acrobatics" in repr(character_skill)
    assert "PROFICIENT" in repr(character_skill)


@patch("app.models.proficiency.CharacterSkill.ability_modifier", new_callable=PropertyMock)
def test_character_skill_modifier_calculation(mock_ability_modifier) -> None:
    """Test calculating the modifier for a character skill."""
    # Set up the mock ability modifier
    mock_ability_modifier.return_value = 3

    proficiency = Proficiency(
        name="Acrobatics", type=ProficiencyType.SKILL, ability_score="Dexterity"
    )

    # Test not proficient (just ability modifier)
    character_skill = CharacterSkill(
        character_id=1,
        proficiency_id=1,
        proficiency_level=ProficiencyLevel.NOT_PROFICIENT,
        proficiency=proficiency,
    )

    # Mock the character's proficiency bonus
    with patch(
        "app.models.proficiency.CharacterSkill.character_proficiency_bonus",
        new_callable=PropertyMock,
    ) as mock_prof_bonus:
        mock_prof_bonus.return_value = 2

        # Not proficient: just ability modifier
        assert character_skill.modifier == 3

        # Change to proficient: ability modifier + proficiency bonus
        character_skill.proficiency_level = ProficiencyLevel.PROFICIENT
        assert character_skill.modifier == 5

        # Change to expertise: ability modifier + 2 * proficiency bonus
        character_skill.proficiency_level = ProficiencyLevel.EXPERTISE
        assert character_skill.modifier == 7
