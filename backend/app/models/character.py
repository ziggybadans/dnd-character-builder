import enum

from app.models.base import BaseModel
from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship


class Alignment(str, enum.Enum):
    """Enum for character alignments."""

    LAWFUL_GOOD = "lawful good"
    NEUTRAL_GOOD = "neutral good"
    CHAOTIC_GOOD = "chaotic good"
    LAWFUL_NEUTRAL = "lawful neutral"
    TRUE_NEUTRAL = "true neutral"
    CHAOTIC_NEUTRAL = "chaotic neutral"
    LAWFUL_EVIL = "lawful evil"
    NEUTRAL_EVIL = "neutral evil"
    CHAOTIC_EVIL = "chaotic evil"


class Character(BaseModel):
    """Model for player characters."""

    # Basic information
    name = Column(String(100), nullable=False, index=True)
    level = Column(Integer, nullable=False, default=1)
    experience_points = Column(Integer, nullable=False, default=0)
    alignment = Column(Enum(Alignment), nullable=False, default=Alignment.TRUE_NEUTRAL)

    # Character details
    age = Column(Integer)
    height = Column(String(50))
    weight = Column(String(50))
    eyes = Column(String(50))
    skin = Column(String(50))
    hair = Column(String(50))

    # Character background
    personality_traits = Column(Text)
    ideals = Column(Text)
    bonds = Column(Text)
    flaws = Column(Text)
    backstory = Column(Text)

    # Character stats
    max_hit_points = Column(Integer, nullable=False, default=0)
    current_hit_points = Column(Integer, nullable=False, default=0)
    temporary_hit_points = Column(Integer, nullable=False, default=0)
    armor_class = Column(Integer, nullable=False, default=10)
    initiative = Column(Integer, nullable=False, default=0)
    speed = Column(Integer, nullable=False, default=30)
    inspiration = Column(Boolean, nullable=False, default=False)

    # Death saves
    death_saves_successes = Column(Integer, nullable=False, default=0)
    death_saves_failures = Column(Integer, nullable=False, default=0)

    # Foreign keys
    race_id = Column(Integer, ForeignKey("race.id"), nullable=False)
    subrace_id = Column(Integer, ForeignKey("subrace.id"))
    background_id = Column(Integer, ForeignKey("background.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))

    # Relationships
    race = relationship("Race", back_populates="characters")
    subrace = relationship("Subrace", back_populates="characters")
    background = relationship("Background", back_populates="characters")
    class_levels = relationship("CharacterClassLevel", back_populates="character")
    ability_scores = relationship("CharacterAbilityScore", back_populates="character")
    skills = relationship("CharacterSkill", back_populates="character")
    proficiencies = relationship(
        "Proficiency", secondary="character_proficiency", back_populates="characters"
    )
    user = relationship("User", back_populates="characters")

    @property
    def proficiency_bonus(self) -> int:
        """Calculate proficiency bonus based on character level."""
        return (self.level - 1) // 4 + 2

    def __repr__(self) -> str:
        return f"<Character {self.name} (Level {self.level})>"
