from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from ..db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class User(Base):

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    jokes = relationship("Joke", back_populates="owner")
    # items = relationship("Item", back_populates="owner")
