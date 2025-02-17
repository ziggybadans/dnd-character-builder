"""Model for player characters."""

from typing import List, Optional

from sqlalchemy import JSON, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .background import Background
from .base import Base, NameDescriptionMixin
from .class_ import Class, Subclass
from .race import Race, Subrace


class Character(Base, NameDescriptionMixin):
    """Model for player characters."""

    __tablename__ = "characters"

    # Basic Information
    level: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    experience_points: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    alignment: Mapped[str] = mapped_column(String(20), nullable=False)

    # Race Information
    race_id: Mapped[int] = mapped_column(ForeignKey("races.id"), nullable=False)
    subrace_id: Mapped[Optional[int]] = mapped_column(ForeignKey("subraces.id"))

    # Class Information
    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"), nullable=False)
    subclass_id: Mapped[Optional[int]] = mapped_column(ForeignKey("subclasses.id"))

    # Background Information
    background_id: Mapped[int] = mapped_column(ForeignKey("backgrounds.id"), nullable=False)

    # Ability Scores
    strength: Mapped[int] = mapped_column(Integer, nullable=False)
    dexterity: Mapped[int] = mapped_column(Integer, nullable=False)
    constitution: Mapped[int] = mapped_column(Integer, nullable=False)
    intelligence: Mapped[int] = mapped_column(Integer, nullable=False)
    wisdom: Mapped[int] = mapped_column(Integer, nullable=False)
    charisma: Mapped[int] = mapped_column(Integer, nullable=False)

    # Character Stats
    hit_points: Mapped[int] = mapped_column(Integer, nullable=False)
    max_hit_points: Mapped[int] = mapped_column(Integer, nullable=False)
    temporary_hit_points: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    armor_class: Mapped[int] = mapped_column(Integer, nullable=False)
    initiative: Mapped[int] = mapped_column(Integer, nullable=False)
    speed: Mapped[int] = mapped_column(Integer, nullable=False)

    # Additional Information
    proficiencies: Mapped[dict] = mapped_column(JSON, nullable=False)
    features: Mapped[dict] = mapped_column(JSON, nullable=False)
    equipment: Mapped[dict] = mapped_column(JSON, nullable=False)
    spells: Mapped[Optional[dict]] = mapped_column(JSON)
    personality: Mapped[dict] = mapped_column(JSON, nullable=False)

    # Relationships
    race: Mapped[Race] = relationship(foreign_keys=[race_id])
    subrace: Mapped[Optional[Subrace]] = relationship(foreign_keys=[subrace_id])
    character_class: Mapped[Class] = relationship(foreign_keys=[class_id])
    subclass: Mapped[Optional[Subclass]] = relationship(foreign_keys=[subclass_id])
    background: Mapped[Background] = relationship()
