"""Unit tests for character class models."""

import pytest
from app.models.character_class import CharacterClass, CharacterClassLevel, ClassFeature, Subclass


def test_character_class_creation() -> None:
    """Test creating a character class."""
    character_class = CharacterClass(
        name="Fighter",
        description="A master of martial combat, skilled with a variety of weapons and armor",
        hit_die=10,
        primary_ability="Strength or Dexterity",
        saving_throw_proficiencies="Strength, Constitution",
        armor_proficiencies="All armor, shields",
        weapon_proficiencies="Simple weapons, martial weapons",
        tool_proficiencies="None",
        skill_proficiencies="Choose two from Acrobatics, Animal Handling, Athletics, History, Insight, Intimidation, Perception, and Survival",
        equipment="(a) chain mail or (b) leather armor, longbow, and 20 arrows; (a) a martial weapon and a shield or (b) two martial weapons; (a) a light crossbow and 20 bolts or (b) two handaxes; (a) a dungeoneer's pack or (b) an explorer's pack",
        spellcasting_ability="None",
        is_spellcaster=False,
        source_book="Player's Handbook",
    )

    assert character_class.name == "Fighter"
    assert (
        character_class.description
        == "A master of martial combat, skilled with a variety of weapons and armor"
    )
    assert character_class.hit_die == 10
    assert character_class.primary_ability == "Strength or Dexterity"
    assert character_class.saving_throw_proficiencies == "Strength, Constitution"
    assert character_class.armor_proficiencies == "All armor, shields"
    assert character_class.weapon_proficiencies == "Simple weapons, martial weapons"
    assert character_class.tool_proficiencies == "None"
    assert (
        character_class.skill_proficiencies
        == "Choose two from Acrobatics, Animal Handling, Athletics, History, Insight, Intimidation, Perception, and Survival"
    )
    assert (
        character_class.equipment
        == "(a) chain mail or (b) leather armor, longbow, and 20 arrows; (a) a martial weapon and a shield or (b) two martial weapons; (a) a light crossbow and 20 bolts or (b) two handaxes; (a) a dungeoneer's pack or (b) an explorer's pack"
    )
    assert character_class.spellcasting_ability == "None"
    assert character_class.is_spellcaster is False
    assert character_class.source_book == "Player's Handbook"
    assert character_class.subclasses == []
    assert character_class.features == []
    assert character_class.levels == []


def test_character_class_repr() -> None:
    """Test the string representation of a character class."""
    character_class = CharacterClass(name="Wizard", hit_die=6, source_book="Player's Handbook")

    assert repr(character_class) == "<CharacterClass Wizard>"


def test_subclass_creation() -> None:
    """Test creating a subclass."""
    character_class = CharacterClass(name="Fighter", hit_die=10, source_book="Player's Handbook")

    subclass = Subclass(
        name="Champion",
        description="The archetypal Champion focuses on the development of raw physical power honed to deadly perfection.",
        character_class=character_class,
        source_book="Player's Handbook",
    )

    assert subclass.name == "Champion"
    assert (
        subclass.description
        == "The archetypal Champion focuses on the development of raw physical power honed to deadly perfection."
    )
    assert subclass.character_class.name == "Fighter"
    assert subclass.source_book == "Player's Handbook"
    assert subclass.features == []


def test_subclass_repr() -> None:
    """Test the string representation of a subclass."""
    character_class = CharacterClass(name="Fighter", hit_die=10, source_book="Player's Handbook")

    subclass = Subclass(
        name="Champion", character_class=character_class, source_book="Player's Handbook"
    )

    assert repr(subclass) == "<Subclass Champion (Fighter)>"


def test_class_feature_creation() -> None:
    """Test creating a class feature."""
    character_class = CharacterClass(name="Fighter", hit_die=10, source_book="Player's Handbook")

    subclass = Subclass(
        name="Champion", character_class=character_class, source_book="Player's Handbook"
    )

    class_feature = ClassFeature(
        name="Second Wind",
        description="You have a limited well of stamina that you can draw on to protect yourself from harm.",
        level=1,
        character_class=character_class,
        subclass=None,
        source_book="Player's Handbook",
    )

    subclass_feature = ClassFeature(
        name="Improved Critical",
        description="Your weapon attacks score a critical hit on a roll of 19 or 20.",
        level=3,
        character_class=character_class,
        subclass=subclass,
        source_book="Player's Handbook",
    )

    assert class_feature.name == "Second Wind"
    assert (
        class_feature.description
        == "You have a limited well of stamina that you can draw on to protect yourself from harm."
    )
    assert class_feature.level == 1
    assert class_feature.character_class.name == "Fighter"
    assert class_feature.subclass is None
    assert class_feature.source_book == "Player's Handbook"

    assert subclass_feature.name == "Improved Critical"
    assert (
        subclass_feature.description
        == "Your weapon attacks score a critical hit on a roll of 19 or 20."
    )
    assert subclass_feature.level == 3
    assert subclass_feature.character_class.name == "Fighter"
    assert subclass_feature.subclass.name == "Champion"
    assert subclass_feature.source_book == "Player's Handbook"


def test_class_feature_repr() -> None:
    """Test the string representation of a class feature."""
    character_class = CharacterClass(name="Fighter", hit_die=10, source_book="Player's Handbook")

    subclass = Subclass(
        name="Champion", character_class=character_class, source_book="Player's Handbook"
    )

    class_feature = ClassFeature(
        name="Second Wind",
        level=1,
        character_class=character_class,
        source_book="Player's Handbook",
    )

    subclass_feature = ClassFeature(
        name="Improved Critical",
        level=3,
        character_class=character_class,
        subclass=subclass,
        source_book="Player's Handbook",
    )

    assert repr(class_feature) == "<ClassFeature Second Wind (Fighter, Level 1)>"
    assert repr(subclass_feature) == "<ClassFeature Improved Critical (Fighter: Champion, Level 3)>"


def test_character_class_level_creation() -> None:
    """Test creating a character class level."""
    character_class = CharacterClass(name="Fighter", hit_die=10, source_book="Player's Handbook")

    class_level = CharacterClassLevel(
        level=1,
        character_class=character_class,
        features="Fighting Style, Second Wind",
        cantrips_known=0,
        spells_known=0,
        spell_slots_level_1=0,
        spell_slots_level_2=0,
        spell_slots_level_3=0,
        spell_slots_level_4=0,
        spell_slots_level_5=0,
        spell_slots_level_6=0,
        spell_slots_level_7=0,
        spell_slots_level_8=0,
        spell_slots_level_9=0,
        source_book="Player's Handbook",
    )

    assert class_level.level == 1
    assert class_level.character_class.name == "Fighter"
    assert class_level.features == "Fighting Style, Second Wind"
    assert class_level.cantrips_known == 0
    assert class_level.spells_known == 0
    assert class_level.spell_slots_level_1 == 0
    assert class_level.spell_slots_level_2 == 0
    assert class_level.spell_slots_level_3 == 0
    assert class_level.spell_slots_level_4 == 0
    assert class_level.spell_slots_level_5 == 0
    assert class_level.spell_slots_level_6 == 0
    assert class_level.spell_slots_level_7 == 0
    assert class_level.spell_slots_level_8 == 0
    assert class_level.spell_slots_level_9 == 0
    assert class_level.source_book == "Player's Handbook"


def test_character_class_level_repr() -> None:
    """Test the string representation of a character class level."""
    character_class = CharacterClass(name="Fighter", hit_die=10, source_book="Player's Handbook")

    class_level = CharacterClassLevel(
        level=1, character_class=character_class, source_book="Player's Handbook"
    )

    assert repr(class_level) == "<CharacterClassLevel Fighter 1>"
