"""Unit tests for database models."""

import pytest
from app.models import Background, Base, Character, Class, Race, Subclass, Subrace
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


@pytest.fixture
def engine():
    """Create a test database engine."""
    return create_engine("sqlite:///:memory:")


@pytest.fixture
def session(engine):
    """Create a new database session for a test."""
    Base.metadata.create_all(engine)
    session = Session(engine)
    yield session
    session.close()
    Base.metadata.drop_all(engine)


def test_race_creation(session):
    """Test creating a race with a subrace."""
    race = Race(
        name="Dwarf",
        description="Bold and hardy folk",
        ability_score_increase={"constitution": 2},
        age={"maturity": 18, "max_age": 350},
        size={"category": "Medium", "height": {"base": 44, "modifier": "2d4"}},
        speed={"walk": 25},
        languages={"standard": ["Common", "Dwarvish"]},
        traits={"darkvision": 60},
        source_book="PHB",
    )
    session.add(race)
    session.commit()

    subrace = Subrace(
        name="Hill Dwarf",
        description="Wise and hardy",
        race_id=race.id,
        ability_score_increase={"wisdom": 1},
        traits={"dwarven_toughness": True},
        source_book="PHB",
    )
    session.add(subrace)
    session.commit()

    assert race.subraces[0].name == "Hill Dwarf"
    assert subrace.parent_race.name == "Dwarf"


def test_class_creation(session):
    """Test creating a class with a subclass."""
    class_ = Class(
        name="Fighter",
        description="Master of martial combat",
        hit_die="d10",
        primary_ability=["strength", "dexterity"],
        saving_throws=["strength", "constitution"],
        proficiencies={
            "armor": ["light", "medium", "heavy"],
            "weapons": ["simple", "martial"],
            "tools": [],
            "skills": {"count": 2, "options": ["Acrobatics", "Athletics"]},
        },
        starting_equipment={"default": [["longsword"], ["shield"]]},
        features_by_level={
            "1": [{"name": "Fighting Style", "description": "Choose a fighting style"}]
        },
        source_book="PHB",
    )
    session.add(class_)
    session.commit()

    subclass = Subclass(
        name="Champion",
        description="Improved critical fighter",
        class_id=class_.id,
        features_by_level={"3": [{"name": "Improved Critical", "description": "Crit on 19-20"}]},
        source_book="PHB",
    )
    session.add(subclass)
    session.commit()

    assert class_.subclasses[0].name == "Champion"
    assert subclass.parent_class.name == "Fighter"


def test_background_creation(session):
    """Test creating a background."""
    background = Background(
        name="Acolyte",
        description="Religious servant",
        proficiencies={"skills": ["Insight", "Religion"], "languages": {"count": 2}},
        equipment=["holy_symbol", "prayer_book"],
        feature={
            "name": "Shelter of the Faithful",
            "description": "Receive aid from religious community",
        },
        characteristics={
            "personality_traits": ["I idolize a hero of my faith"],
            "ideals": ["Faith. I trust that my deity will guide my actions"],
            "bonds": ["I would die to recover a sacred relic"],
            "flaws": ["I judge others harshly"],
        },
        source_book="PHB",
    )
    session.add(background)
    session.commit()

    assert background.name == "Acolyte"
    assert "holy_symbol" in background.equipment


def test_character_creation(session):
    """Test creating a complete character."""
    # Create required related objects
    race = Race(
        name="Dwarf",
        description="Bold and hardy folk",
        ability_score_increase={"constitution": 2},
        age={"maturity": 18, "max_age": 350},
        size={"category": "Medium", "height": {"base": 44, "modifier": "2d4"}},
        speed={"walk": 25},
        languages={"standard": ["Common", "Dwarvish"]},
        traits={"darkvision": 60},
        source_book="PHB",
    )
    class_ = Class(
        name="Fighter",
        description="Master of martial combat",
        hit_die="d10",
        primary_ability=["strength", "dexterity"],
        saving_throws=["strength", "constitution"],
        proficiencies={
            "armor": ["light", "medium", "heavy"],
            "weapons": ["simple", "martial"],
            "tools": [],
            "skills": {"count": 2, "options": ["Acrobatics", "Athletics"]},
        },
        starting_equipment={"default": [["longsword"], ["shield"]]},
        features_by_level={
            "1": [{"name": "Fighting Style", "description": "Choose a fighting style"}]
        },
        source_book="PHB",
    )
    background = Background(
        name="Acolyte",
        description="Religious servant",
        proficiencies={"skills": ["Insight", "Religion"], "languages": {"count": 2}},
        equipment=["holy_symbol", "prayer_book"],
        feature={
            "name": "Shelter of the Faithful",
            "description": "Receive aid from religious community",
        },
        characteristics={
            "personality_traits": ["I idolize a hero of my faith"],
            "ideals": ["Faith. I trust that my deity will guide my actions"],
            "bonds": ["I would die to recover a sacred relic"],
            "flaws": ["I judge others harshly"],
        },
        source_book="PHB",
    )

    session.add_all([race, class_, background])
    session.commit()

    character = Character(
        name="Thorin Ironfist",
        description="A devout dwarven warrior",
        level=1,
        experience_points=0,
        alignment="Lawful Good",
        race_id=race.id,
        class_id=class_.id,
        background_id=background.id,
        strength=16,
        dexterity=12,
        constitution=16,
        intelligence=10,
        wisdom=13,
        charisma=8,
        hit_points=12,
        max_hit_points=12,
        armor_class=16,
        initiative=1,
        speed=25,
        proficiencies={
            "armor": ["light", "medium", "heavy"],
            "weapons": ["simple", "martial"],
            "skills": ["Athletics", "Religion"],
        },
        features={"fighting_style": "Defense"},
        equipment={"weapons": ["longsword", "shield"], "armor": ["chain_mail"]},
        personality={
            "traits": ["I am always polite and respectful"],
            "ideals": ["Honor. A deal is a deal"],
            "bonds": ["My clan is everything to me"],
            "flaws": ["I am suspicious of strangers"],
        },
    )
    session.add(character)
    session.commit()

    assert character.name == "Thorin Ironfist"
    assert character.race.name == "Dwarf"
    assert character.character_class.name == "Fighter"
    assert character.background.name == "Acolyte"
    assert character.level == 1
    assert character.hit_points == 12
