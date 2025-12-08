import uuid

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseTable
from .bucket import Bucket


class User(BaseTable):
    __tablename__ = "users"
