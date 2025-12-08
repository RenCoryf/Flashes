from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Card(Base):
    __tablename__ = "cards"

    title: Mapped[str] = mapped_column(String(127), nullable=False)
    question: Mapped[str] = mapped_column(String(4095), nullable=True)
    answer: Mapped[str] = mapped_column(String(4095), nullable=True)

    bucket_id: Mapped[int] = mapped_column(Integer, ForeignKey("buckets.id"), nullable=False)

    bucket: Mapped["Bucket"] = relationship(back_populates="cards")

    def __repr__(self):
        return f"<Card(id={self.id}, title='{self.title}')>"
