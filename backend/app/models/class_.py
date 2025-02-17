"""Models for classes and subclasses."""

from typing import List, Optional

from sqlalchemy import JSON, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, NameDescriptionMixin


class Class(Base, NameDescriptionMixin):
    """Model for character classes."""

    __tablename__ = "classes"

    hit_die: Mapped[str] = mapped_column(String(4), nullable=False)
    primary_ability: Mapped[List[str]] = mapped_column(JSON, nullable=False)
    saving_throws: Mapped[List[str]] = mapped_column(JSON, nullable=False)
    proficiencies: Mapped[dict] = mapped_column(JSON, nullable=False)
    starting_equipment: Mapped[dict] = mapped_column(JSON, nullable=False)
    spellcasting_ability: Mapped[Optional[str]] = mapped_column(String(20))
    spell_slots_progression: Mapped[Optional[dict]] = mapped_column(JSON)
    features_by_level: Mapped[dict] = mapped_column(JSON, nullable=False)
    source_book: Mapped[str] = mapped_column(String(50), nullable=False)

    # Relationships
    subclasses: Mapped[List["Subclass"]] = relationship(
        back_populates="parent_class", cascade="all, delete-orphan"
    )


class Subclass(Base, NameDescriptionMixin):
    """Model for character subclasses."""

    __tablename__ = "subclasses"

    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"), nullable=False)
    features_by_level: Mapped[dict] = mapped_column(JSON, nullable=False)
    spellcasting_ability: Mapped[Optional[str]] = mapped_column(String(20))
    source_book: Mapped[str] = mapped_column(String(50), nullable=False)

    # Relationships
    parent_class: Mapped[Class] = relationship(back_populates="subclasses")
