"""Models for races and subraces."""

from typing import List, Optional

from sqlalchemy import JSON, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, NameDescriptionMixin


class Race(Base, NameDescriptionMixin):
    """Model for character races."""

    __tablename__ = "races"

    ability_score_increase: Mapped[dict] = mapped_column(JSON, nullable=False)
    age: Mapped[dict] = mapped_column(JSON, nullable=False)
    size: Mapped[dict] = mapped_column(JSON, nullable=False)
    speed: Mapped[dict] = mapped_column(JSON, nullable=False)
    languages: Mapped[dict] = mapped_column(JSON, nullable=False)
    traits: Mapped[dict] = mapped_column(JSON, nullable=False)
    source_book: Mapped[str] = mapped_column(String(50), nullable=False)

    # Relationships
    subraces: Mapped[List["Subrace"]] = relationship(
        back_populates="parent_race", cascade="all, delete-orphan"
    )


class Subrace(Base, NameDescriptionMixin):
    """Model for character subraces."""

    __tablename__ = "subraces"

    race_id: Mapped[int] = mapped_column(ForeignKey("races.id"), nullable=False)
    ability_score_increase: Mapped[dict] = mapped_column(JSON, nullable=False)
    traits: Mapped[dict] = mapped_column(JSON, nullable=False)
    source_book: Mapped[str] = mapped_column(String(50), nullable=False)

    # Relationships
    parent_race: Mapped[Race] = relationship(back_populates="subraces")
