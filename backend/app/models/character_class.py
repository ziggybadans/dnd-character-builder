from app.models.base import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

# Association table for class-feature relationship
class_feature = Table(
    "class_feature",
    BaseModel.metadata,
    Column("class_id", Integer, ForeignKey("characterclass.id"), primary_key=True),
    Column("feature_id", Integer, ForeignKey("classfeature.id"), primary_key=True),
)

# Association table for subclass-feature relationship
subclass_feature = Table(
    "subclass_feature",
    BaseModel.metadata,
    Column("subclass_id", Integer, ForeignKey("subclass.id"), primary_key=True),
    Column("feature_id", Integer, ForeignKey("classfeature.id"), primary_key=True),
)

# Association table for class-proficiency relationship
class_proficiency = Table(
    "class_proficiency",
    BaseModel.metadata,
    Column("class_id", Integer, ForeignKey("characterclass.id"), primary_key=True),
    Column("proficiency_id", Integer, ForeignKey("proficiency.id"), primary_key=True),
)


class CharacterClass(BaseModel):
    """Model for character classes (Fighter, Wizard, Cleric, etc.)."""

    name = Column(String(100), nullable=False, index=True, unique=True)
    description = Column(String(1000), nullable=False)
    hit_die = Column(Integer, nullable=False)  # e.g., 8 for d8, 10 for d10
    primary_ability = Column(String(100), nullable=False)
    saving_throw_proficiencies = Column(String(100), nullable=False)
    armor_proficiencies = Column(String(200))
    weapon_proficiencies = Column(String(200))
    tool_proficiencies = Column(String(200))
    skill_proficiencies = Column(String(500))
    equipment = Column(String(500))
    spellcasting_ability = Column(String(50))
    is_spellcaster = Column(Boolean, default=False)
    source_book = Column(String(100), nullable=False, default="Player's Handbook")
    source_page = Column(Integer)

    # Relationships
    subclasses = relationship("Subclass", back_populates="character_class")
    features = relationship("ClassFeature", secondary=class_feature, back_populates="classes")
    proficiencies = relationship(
        "Proficiency", secondary=class_proficiency, back_populates="character_classes"
    )
    levels = relationship("CharacterClassLevel", back_populates="character_class")

    def __repr__(self) -> str:
        return f"<CharacterClass {self.name}>"


class Subclass(BaseModel):
    """Model for character subclasses (Champion, School of Evocation, etc.)."""

    name = Column(String(100), nullable=False, index=True, unique=True)
    description = Column(String(1000), nullable=False)
    class_id = Column(Integer, ForeignKey("characterclass.id"), nullable=False)
    source_book = Column(String(100), nullable=False, default="Player's Handbook")
    source_page = Column(Integer)

    # Relationships
    character_class = relationship("CharacterClass", back_populates="subclasses")
    features = relationship("ClassFeature", secondary=subclass_feature, back_populates="subclasses")
    character_subclasses = relationship("CharacterClassLevel", back_populates="subclass")

    def __repr__(self) -> str:
        return f"<Subclass {self.name} ({self.character_class.name if self.character_class else 'Unknown'})>"


class ClassFeature(BaseModel):
    """Model for class features (Action Surge, Rage, etc.)."""

    name = Column(String(100), nullable=False, index=True)
    description = Column(String(1000), nullable=False)
    level = Column(Integer, nullable=False)
    is_optional = Column(Boolean, default=False)
    source_book = Column(String(100), nullable=False, default="Player's Handbook")
    source_page = Column(Integer)
    character_class_id = Column(Integer, ForeignKey("characterclass.id"))
    subclass_id = Column(Integer, ForeignKey("subclass.id"))

    # Relationships
    classes = relationship("CharacterClass", secondary=class_feature, back_populates="features")
    subclasses = relationship("Subclass", secondary=subclass_feature, back_populates="features")
    character_class = relationship("CharacterClass", foreign_keys=[character_class_id])
    subclass = relationship("Subclass", foreign_keys=[subclass_id])

    def __repr__(self) -> str:
        if self.character_class and self.subclass:
            return f"<ClassFeature {self.name} ({self.character_class.name}: {self.subclass.name}, Level {self.level})>"
        elif self.character_class:
            return f"<ClassFeature {self.name} ({self.character_class.name}, Level {self.level})>"
        else:
            return f"<ClassFeature {self.name} (Level {self.level})>"


class CharacterClassLevel(BaseModel):
    """Model for tracking a character's class levels."""

    character_id = Column(Integer, ForeignKey("character.id"), nullable=False)
    class_id = Column(Integer, ForeignKey("characterclass.id"), nullable=False)
    subclass_id = Column(Integer, ForeignKey("subclass.id"))
    level = Column(Integer, nullable=False, default=1)
    is_primary = Column(Boolean, default=True)
    features = Column(String(500))
    cantrips_known = Column(Integer, default=0)
    spells_known = Column(Integer, default=0)
    spell_slots_level_1 = Column(Integer, default=0)
    spell_slots_level_2 = Column(Integer, default=0)
    spell_slots_level_3 = Column(Integer, default=0)
    spell_slots_level_4 = Column(Integer, default=0)
    spell_slots_level_5 = Column(Integer, default=0)
    spell_slots_level_6 = Column(Integer, default=0)
    spell_slots_level_7 = Column(Integer, default=0)
    spell_slots_level_8 = Column(Integer, default=0)
    spell_slots_level_9 = Column(Integer, default=0)
    source_book = Column(String(100), nullable=False, default="Player's Handbook")

    # Relationships
    character = relationship("Character", back_populates="class_levels")
    character_class = relationship("CharacterClass", back_populates="levels")
    subclass = relationship("Subclass", back_populates="character_subclasses")

    def __repr__(self) -> str:
        class_name = self.character_class.name if self.character_class else "Unknown"
        return f"<CharacterClassLevel {class_name} {self.level}>"
