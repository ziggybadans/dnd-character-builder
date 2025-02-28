import enum

from app.models.base import BaseModel
from sqlalchemy import Column, Enum, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

# Association table for character-proficiency relationship
character_proficiency = Table(
    "character_proficiency",
    BaseModel.metadata,
    Column("character_id", Integer, ForeignKey("character.id"), primary_key=True),
    Column("proficiency_id", Integer, ForeignKey("proficiency.id"), primary_key=True),
)


class ProficiencyType(str, enum.Enum):
    """Enum for proficiency types."""

    SKILL = "skill"
    ARMOR = "armor"
    WEAPON = "weapon"
    TOOL = "tool"
    SAVING_THROW = "saving_throw"
    LANGUAGE = "language"


class ProficiencyLevel(str, enum.Enum):
    """Enum for proficiency levels."""

    NOT_PROFICIENT = "not_proficient"
    PROFICIENT = "proficient"
    EXPERTISE = "expertise"


class Proficiency(BaseModel):
    """Model for proficiencies (skills, tools, weapons, etc.)."""

    name = Column(String(100), nullable=False, index=True, unique=True)
    description = Column(String(500))
    type = Column(Enum(ProficiencyType), nullable=False)
    ability_score = Column(String(50))  # For skills, which ability score they're based on

    # Relationships
    characters = relationship(
        "Character", secondary=character_proficiency, back_populates="proficiencies"
    )
    character_classes = relationship(
        "CharacterClass", secondary="class_proficiency", back_populates="proficiencies"
    )
    backgrounds = relationship(
        "Background", secondary="background_proficiency", back_populates="proficiencies"
    )
    races = relationship("Race", secondary="race_proficiency", back_populates="proficiencies")

    def __repr__(self) -> str:
        return f"<Proficiency {self.name} ({self.type})>"


class CharacterSkill(BaseModel):
    """Model for character skills with proficiency and expertise tracking."""

    character_id = Column(Integer, ForeignKey("character.id"), nullable=False)
    proficiency_id = Column(Integer, ForeignKey("proficiency.id"), nullable=False)
    is_proficient = Column(Integer, default=0)  # 0: not proficient, 1: proficient, 2: expertise
    proficiency_level = Column(Enum(ProficiencyLevel), default=ProficiencyLevel.NOT_PROFICIENT)

    # Relationships
    character = relationship("Character", back_populates="skills")
    proficiency = relationship("Proficiency")

    @property
    def ability_modifier(self) -> int:
        """Get the ability modifier for this skill."""
        if not self.character or not self.proficiency:
            return 0

        # Find the relevant ability score
        ability_score_name = self.proficiency.ability_score
        if not ability_score_name:
            return 0

        # Find the character's ability score
        for char_ability in self.character.ability_scores:
            if char_ability.ability_score.name.lower() == ability_score_name.lower():
                return char_ability.modifier

        return 0

    @property
    def character_proficiency_bonus(self) -> int:
        """Get the character's proficiency bonus."""
        if not self.character:
            return 0
        return self.character.proficiency_bonus

    @property
    def modifier(self) -> int:
        """Calculate the skill modifier based on ability score and proficiency."""
        ability_modifier = self.ability_modifier

        # Apply proficiency or expertise if applicable
        if self.proficiency_level == ProficiencyLevel.PROFICIENT:
            return ability_modifier + self.character_proficiency_bonus
        elif self.proficiency_level == ProficiencyLevel.EXPERTISE:
            return ability_modifier + (self.character_proficiency_bonus * 2)
        else:  # Not proficient
            return ability_modifier

    def __repr__(self) -> str:
        proficiency_name = self.proficiency.name if self.proficiency else "Unknown"
        return f"<CharacterSkill {proficiency_name} ({self.proficiency_level})>"
