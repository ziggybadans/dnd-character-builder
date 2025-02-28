from app.models.base import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class AbilityScore(BaseModel):
    """Model for character ability scores (Strength, Dexterity, etc.)."""

    name = Column(String(50), nullable=False, index=True)
    abbreviation = Column(String(3), nullable=False)
    description = Column(String(500), nullable=False)

    # Relationships
    character_ability_scores = relationship("CharacterAbilityScore", back_populates="ability_score")

    def __repr__(self) -> str:
        return f"<AbilityScore {self.name}>"


class CharacterAbilityScore(BaseModel):
    """Model for a character's ability score values."""

    character_id = Column(Integer, ForeignKey("character.id"), nullable=False)
    ability_score_id = Column(Integer, ForeignKey("abilityscore.id"), nullable=False)
    base_value = Column(Integer, nullable=False)
    racial_bonus = Column(Integer, default=0)
    asi_bonus = Column(Integer, default=0)  # Ability Score Improvement
    misc_bonus = Column(Integer, default=0)

    # Relationships
    character = relationship("Character", back_populates="ability_scores")
    ability_score = relationship("AbilityScore", back_populates="character_ability_scores")

    @property
    def total_value(self) -> int:
        """Calculate the total ability score value."""
        return self.base_value + self.racial_bonus + self.asi_bonus + self.misc_bonus

    @property
    def modifier(self) -> int:
        """Calculate the ability score modifier."""
        return (self.total_value - 10) // 2

    def __repr__(self) -> str:
        return f"<CharacterAbilityScore {self.character_id}:{self.ability_score.name if self.ability_score else 'Unknown'}>"
