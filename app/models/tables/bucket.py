import uuid

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseTable
from .card import Card


class Bucket(BaseTable):
    __tablename__ = "buckets"

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    theme: Mapped[str] = mapped_column(String(255), nullable=True)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    course: Mapped[int] = mapped_column(Integer, ForeignKey("courses.id"), nullable=False)
    uni: Mapped[str] = mapped_column(String, ForeignKey("universities.id"), nullable=False)
    cards_amount: Mapped[int] = mapped_column(Integer, default=0)

    user: Mapped["User"] = relationship(back_populates="buckets")
    cards: Mapped["Card"] = relationship(back_populates="bucket")

    def __repr__(self):
        return f"<Bucket(id={self.id}, name='{self.name}')>"
