"""Model for character backgrounds."""

from typing import List

from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, NameDescriptionMixin


class Background(Base, NameDescriptionMixin):
    """Model for character backgrounds."""

    __tablename__ = "backgrounds"

    proficiencies: Mapped[dict] = mapped_column(JSON, nullable=False)
    equipment: Mapped[List[str]] = mapped_column(JSON, nullable=False)
    feature: Mapped[dict] = mapped_column(JSON, nullable=False)
    characteristics: Mapped[dict] = mapped_column(JSON, nullable=False)
    source_book: Mapped[str] = mapped_column(String(50), nullable=False)
