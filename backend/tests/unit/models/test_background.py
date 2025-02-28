"""Unit tests for background models."""

import pytest
from app.models.background import Background, BackgroundFeature


def test_background_creation() -> None:
    """Test creating a background."""
    background = Background(
        name="Acolyte",
        description="You have spent your life in the service of a temple to a specific god or pantheon of gods",
        skill_proficiencies="Insight, Religion",
        languages="Two of your choice",
        equipment="A holy symbol, a prayer book, 5 sticks of incense, vestments, a set of common clothes, and a pouch containing 15 gp",
        suggested_characteristics="Acolytes are shaped by their experience in temples or other religious communities",
        source_book="Player's Handbook",  # Explicitly set the source book
    )

    assert background.name == "Acolyte"
    assert (
        background.description
        == "You have spent your life in the service of a temple to a specific god or pantheon of gods"
    )
    assert background.skill_proficiencies == "Insight, Religion"
    assert background.languages == "Two of your choice"
    assert (
        background.equipment
        == "A holy symbol, a prayer book, 5 sticks of incense, vestments, a set of common clothes, and a pouch containing 15 gp"
    )
    assert (
        background.suggested_characteristics
        == "Acolytes are shaped by their experience in temples or other religious communities"
    )
    assert background.source_book == "Player's Handbook"
    assert background.proficiencies == []
    assert background.features == []
    assert background.characters == []


def test_background_repr() -> None:
    """Test the string representation of a background."""
    background = Background(
        name="Criminal",
        description="You are an experienced criminal with a history of breaking the law",
    )

    assert repr(background) == "<Background Criminal>"


def test_background_feature_creation() -> None:
    """Test creating a background feature."""
    feature = BackgroundFeature(
        name="Shelter of the Faithful",
        description="As an acolyte, you command the respect of those who share your faith",
        source_book="Player's Handbook",  # Explicitly set the source book
    )

    assert feature.name == "Shelter of the Faithful"
    assert (
        feature.description
        == "As an acolyte, you command the respect of those who share your faith"
    )
    assert feature.source_book == "Player's Handbook"
    assert feature.backgrounds == []


def test_background_feature_repr() -> None:
    """Test the string representation of a background feature."""
    feature = BackgroundFeature(
        name="Criminal Contact",
        description="You have a reliable and trustworthy contact who acts as your liaison to a network of other criminals",
    )

    assert repr(feature) == "<BackgroundFeature Criminal Contact>"
