from app.models.base import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

# Association table for race-trait relationship
race_trait = Table(
    "race_trait",
    BaseModel.metadata,
    Column("race_id", Integer, ForeignKey("race.id"), primary_key=True),
    Column("trait_id", Integer, ForeignKey("racialtrait.id"), primary_key=True),
)

# Association table for subrace-trait relationship
subrace_trait = Table(
    "subrace_trait",
    BaseModel.metadata,
    Column("subrace_id", Integer, ForeignKey("subrace.id"), primary_key=True),
    Column("trait_id", Integer, ForeignKey("racialtrait.id"), primary_key=True),
)

# Association table for race-ability score bonus
race_ability_bonus = Table(
    "race_ability_bonus",
    BaseModel.metadata,
    Column("race_id", Integer, ForeignKey("race.id"), primary_key=True),
    Column("ability_score_id", Integer, ForeignKey("abilityscore.id"), primary_key=True),
    Column("bonus_value", Integer, nullable=False, default=0),
)

# Association table for subrace-ability score bonus
subrace_ability_bonus = Table(
    "subrace_ability_bonus",
    BaseModel.metadata,
    Column("subrace_id", Integer, ForeignKey("subrace.id"), primary_key=True),
    Column("ability_score_id", Integer, ForeignKey("abilityscore.id"), primary_key=True),
    Column("bonus_value", Integer, nullable=False, default=0),
)

# Association table for race-proficiency relationship
race_proficiency = Table(
    "race_proficiency",
    BaseModel.metadata,
    Column("race_id", Integer, ForeignKey("race.id"), primary_key=True),
    Column("proficiency_id", Integer, ForeignKey("proficiency.id"), primary_key=True),
)


class Race(BaseModel):
    """Model for character races (Human, Elf, Dwarf, etc.)."""

    name = Column(String(100), nullable=False, index=True, unique=True)
    description = Column(String(1000), nullable=False)
    speed = Column(Integer, nullable=False, default=30)
    size = Column(String(50), nullable=False, default="Medium")
    age_description = Column(String(500))
    alignment_description = Column(String(500))
    source_book = Column(String(100), nullable=False, default="Player's Handbook")
    source_page = Column(Integer)

    # Relationships
    subraces = relationship("Subrace", back_populates="race")
    traits = relationship("RacialTrait", secondary=race_trait, back_populates="races")
    ability_bonuses = relationship("AbilityScore", secondary=race_ability_bonus)
    characters = relationship("Character", back_populates="race")
    proficiencies = relationship("Proficiency", secondary=race_proficiency, back_populates="races")

    def __repr__(self) -> str:
        return f"<Race {self.name}>"


class Subrace(BaseModel):
    """Model for character subraces (High Elf, Hill Dwarf, etc.)."""

    name = Column(String(100), nullable=False, index=True, unique=True)
    description = Column(String(1000), nullable=False)
    race_id = Column(Integer, ForeignKey("race.id"), nullable=False)
    source_book = Column(String(100), nullable=False, default="Player's Handbook")
    source_page = Column(Integer)

    # Relationships
    race = relationship("Race", back_populates="subraces")
    traits = relationship("RacialTrait", secondary=subrace_trait, back_populates="subraces")
    ability_bonuses = relationship("AbilityScore", secondary=subrace_ability_bonus)
    characters = relationship("Character", back_populates="subrace")

    def __repr__(self) -> str:
        return f"<Subrace {self.name} ({self.race.name if self.race else 'Unknown'})>"


class RacialTrait(BaseModel):
    """Model for racial traits (Darkvision, Fey Ancestry, etc.)."""

    name = Column(String(100), nullable=False, index=True, unique=True)
    description = Column(String(1000), nullable=False)
    is_proficiency = Column(Boolean, default=False)

    # Relationships
    races = relationship("Race", secondary=race_trait, back_populates="traits")
    subraces = relationship("Subrace", secondary=subrace_trait, back_populates="traits")

    def __repr__(self) -> str:
        return f"<RacialTrait {self.name}>"
