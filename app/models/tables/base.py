import uuid
from typing import Any

from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func


class BaseTable(DeclarativeBase):
    __abstract__ = True

    def get_fields_and_values(self):
        mapper = inspect(self.__class__)
        return {col.key: getattr(self, col.key) for col in mapper.columns}

    def to_dict(self) -> dict[str, Any]:
        args = self.get_fields_and_values()
        for key, value in args.items():
            if value is None:
                args[key] = args[key].default
        return args

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
        index=True,
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        onupdate=func.now(),
        server_default=func.now(),
        nullable=False,
    )
