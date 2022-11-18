from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db.base_class import Base

if TYPE_CHECKING:
    from .user import Users  # noqa: F401


class Joke(Base):

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    # owner = relationship("User", back_populates="jokes")
