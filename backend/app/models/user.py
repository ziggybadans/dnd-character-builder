from app.models.base import BaseModel
from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship


class User(BaseModel):
    """Model for application users."""

    username = Column(String(100), nullable=False, index=True, unique=True)
    email = Column(String(100), nullable=False, index=True, unique=True)
    hashed_password = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    # Relationships
    characters = relationship("Character", back_populates="user")

    def __repr__(self) -> str:
        return f"<User {self.username}>"
