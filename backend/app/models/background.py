from app.models.base import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

# Association table for background-proficiency relationship
background_proficiency = Table(
    "background_proficiency",
    BaseModel.metadata,
    Column("background_id", Integer, ForeignKey("background.id"), primary_key=True),
    Column("proficiency_id", Integer, ForeignKey("proficiency.id"), primary_key=True),
)

# Association table for background-feature relationship
background_feature = Table(
    "background_feature",
    BaseModel.metadata,
    Column("background_id", Integer, ForeignKey("background.id"), primary_key=True),
    Column("feature_id", Integer, ForeignKey("backgroundfeature.id"), primary_key=True),
)


class Background(BaseModel):
    """Model for character backgrounds (Acolyte, Criminal, etc.)."""

    name = Column(String(100), nullable=False, index=True, unique=True)
    description = Column(String(1000), nullable=False)
    skill_proficiencies = Column(String(200))
    tool_proficiencies = Column(String(200))
    languages = Column(String(200))
    equipment = Column(String(500))
    suggested_characteristics = Column(String(1000))
    source_book = Column(String(100), nullable=False, default="Player's Handbook")
    source_page = Column(Integer)

    # Relationships
    proficiencies = relationship(
        "Proficiency", secondary=background_proficiency, back_populates="backgrounds"
    )
    features = relationship(
        "BackgroundFeature", secondary=background_feature, back_populates="backgrounds"
    )
    characters = relationship("Character", back_populates="background")

    def __repr__(self) -> str:
        return f"<Background {self.name}>"


class BackgroundFeature(BaseModel):
    """Model for background features (Shelter of the Faithful, Criminal Contact, etc.)."""

    name = Column(String(100), nullable=False, index=True, unique=True)
    description = Column(String(1000), nullable=False)
    source_book = Column(String(100), nullable=False, default="Player's Handbook")
    source_page = Column(Integer)

    # Relationships
    backgrounds = relationship(
        "Background", secondary=background_feature, back_populates="features"
    )

    def __repr__(self) -> str:
        return f"<BackgroundFeature {self.name}>"
