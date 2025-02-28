"""Unit tests for race models."""

import pytest
from app.models.race import Race, RacialTrait, Subrace


def test_race_creation() -> None:
    """Test creating a race."""
    race = Race(
        name="Elf",
        description="Magical people of otherworldly grace",
        speed=30,
        size="Medium",
        age_description="Elves can live to be over 700 years old",
        alignment_description="Elves love freedom, variety, and self-expression",
        source_book="Player's Handbook",  # Explicitly set the source book
    )

    assert race.name == "Elf"
    assert race.description == "Magical people of otherworldly grace"
    assert race.speed == 30
    assert race.size == "Medium"
    assert race.age_description == "Elves can live to be over 700 years old"
    assert race.alignment_description == "Elves love freedom, variety, and self-expression"
    assert race.source_book == "Player's Handbook"
    assert race.subraces == []
    assert race.traits == []
    assert race.ability_bonuses == []
    assert race.characters == []


def test_race_repr() -> None:
    """Test the string representation of a race."""
    race = Race(name="Dwarf", description="Bold and hardy")

    assert repr(race) == "<Race Dwarf>"


def test_subrace_creation() -> None:
    """Test creating a subrace."""
    race = Race(name="Elf", description="Magical people of otherworldly grace")
    subrace = Subrace(
        name="High Elf",
        description="As a high elf, you have a keen mind",
        race_id=1,
        race=race,
        source_book="Player's Handbook",  # Explicitly set the source book
    )

    assert subrace.name == "High Elf"
    assert subrace.description == "As a high elf, you have a keen mind"
    assert subrace.race_id == 1
    assert subrace.race.name == "Elf"
    assert subrace.source_book == "Player's Handbook"
    assert subrace.traits == []
    assert subrace.ability_bonuses == []
    assert subrace.characters == []


def test_subrace_repr() -> None:
    """Test the string representation of a subrace."""
    race = Race(name="Elf", description="Magical people of otherworldly grace")
    subrace = Subrace(
        name="Wood Elf", description="As a wood elf, you have keen senses and intuition", race=race
    )

    assert repr(subrace) == "<Subrace Wood Elf (Elf)>"

    # Test without race
    subrace2 = Subrace(name="Drow", description="Descended from an earlier subrace")
    assert repr(subrace2) == "<Subrace Drow (Unknown)>"


def test_racial_trait_creation() -> None:
    """Test creating a racial trait."""
    trait = RacialTrait(
        name="Darkvision",
        description="You can see in dim light within 60 feet of you as if it were bright light",
        is_proficiency=False,
    )

    assert trait.name == "Darkvision"
    assert (
        trait.description
        == "You can see in dim light within 60 feet of you as if it were bright light"
    )
    assert trait.is_proficiency is False
    assert trait.races == []
    assert trait.subraces == []


def test_racial_trait_repr() -> None:
    """Test the string representation of a racial trait."""
    trait = RacialTrait(
        name="Fey Ancestry", description="You have advantage on saving throws against being charmed"
    )

    assert repr(trait) == "<RacialTrait Fey Ancestry>"
