"""Test configuration and fixtures."""

import pytest
from app.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


@pytest.fixture(scope="session")
def engine():
    """Create a test database engine."""
    return create_engine("sqlite:///:memory:")


@pytest.fixture(scope="session")
def tables(engine):
    """Create all tables for testing."""
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture
def db_session(engine, tables):
    """Create a new database session for a test."""
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture
def sample_race_data():
    """Sample race data for testing."""
    return {
        "name": "Dwarf",
        "description": "Bold and hardy folk",
        "ability_score_increase": {"constitution": 2},
        "age": {"maturity": 18, "max_age": 350},
        "size": {"category": "Medium", "height": {"base": 44, "modifier": "2d4"}},
        "speed": {"walk": 25},
        "languages": {"standard": ["Common", "Dwarvish"]},
        "traits": {"darkvision": 60},
        "source_book": "PHB",
    }


@pytest.fixture
def sample_subrace_data():
    """Sample subrace data for testing."""
    return {
        "name": "Hill Dwarf",
        "description": "Wise and hardy",
        "ability_score_increase": {"wisdom": 1},
        "traits": {"dwarven_toughness": True},
        "source_book": "PHB",
    }


@pytest.fixture
def sample_class_data():
    """Sample class data for testing."""
    return {
        "name": "Fighter",
        "description": "Master of martial combat",
        "hit_die": "d10",
        "primary_ability": ["strength", "dexterity"],
        "saving_throws": ["strength", "constitution"],
        "proficiencies": {
            "armor": ["light", "medium", "heavy"],
            "weapons": ["simple", "martial"],
            "tools": [],
            "skills": {"count": 2, "options": ["Acrobatics", "Athletics"]},
        },
        "starting_equipment": {"default": [["longsword"], ["shield"]]},
        "features_by_level": {
            "1": [{"name": "Fighting Style", "description": "Choose a fighting style"}]
        },
        "source_book": "PHB",
    }


@pytest.fixture
def sample_subclass_data():
    """Sample subclass data for testing."""
    return {
        "name": "Champion",
        "description": "Improved critical fighter",
        "features_by_level": {"3": [{"name": "Improved Critical", "description": "Crit on 19-20"}]},
        "source_book": "PHB",
    }


@pytest.fixture
def sample_background_data():
    """Sample background data for testing."""
    return {
        "name": "Acolyte",
        "description": "Religious servant",
        "proficiencies": {"skills": ["Insight", "Religion"], "languages": {"count": 2}},
        "equipment": ["holy_symbol", "prayer_book"],
        "feature": {
            "name": "Shelter of the Faithful",
            "description": "Receive aid from religious community",
        },
        "characteristics": {
            "personality_traits": ["I idolize a hero of my faith"],
            "ideals": ["Faith. I trust that my deity will guide my actions"],
            "bonds": ["I would die to recover a sacred relic"],
            "flaws": ["I judge others harshly"],
        },
        "source_book": "PHB",
    }


@pytest.fixture
def sample_character_data():
    """Sample character data for testing."""
    return {
        "name": "Thorin Ironfist",
        "description": "A devout dwarven warrior",
        "level": 1,
        "experience_points": 0,
        "alignment": "Lawful Good",
        "strength": 16,
        "dexterity": 12,
        "constitution": 16,
        "intelligence": 10,
        "wisdom": 13,
        "charisma": 8,
        "hit_points": 12,
        "max_hit_points": 12,
        "armor_class": 16,
        "initiative": 1,
        "speed": 25,
        "proficiencies": {
            "armor": ["light", "medium", "heavy"],
            "weapons": ["simple", "martial"],
            "skills": ["Athletics", "Religion"],
        },
        "features": {"fighting_style": "Defense"},
        "equipment": {"weapons": ["longsword", "shield"], "armor": ["chain_mail"]},
        "personality": {
            "traits": ["I am always polite and respectful"],
            "ideals": ["Honor. A deal is a deal"],
            "bonds": ["My clan is everything to me"],
            "flaws": ["I am suspicious of strangers"],
        },
    }
