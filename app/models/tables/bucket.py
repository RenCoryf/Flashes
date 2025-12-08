from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Bucket(Base):
    __tablename__ = "buckets"

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    : Mapped[str] = mapped_column(String(255), nullable=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="buckets")

    def __repr__(self):
        return f"<Bucket(id={self.id}, name='{self.name}')>"
