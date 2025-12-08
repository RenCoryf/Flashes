from abc import ABC
from typing import Any, Generic, Sequence, TypeVar, overload
from uuid import UUID

from sqlalchemy import (
    delete as sql_delete,
)
from sqlalchemy import (
    select as sql_select,
)
from sqlalchemy import (
    update as sql_update,
)
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.tables import Base

T = TypeVar("T", bound=Base)


class BaseDAO(Generic[T], ABC):
    def __init__(self, model: type[T], session: AsyncSession) -> None:
        self._model: type[T] = model
        self._session: AsyncSession = session

    async def create(self, object: T) -> T | None:
        self._session.add(object)
        await self._session.flush()
        return object

    async def update(self, object: T) -> None:
        query = (
            sql_update(self._model)
            .where(self._model.id == object.id)
            .values(object.to_dict())
        )
        _ = await self._session.execute(query)

    @overload
    async def delete(self, object: T) -> None: ...
    @overload
    async def delete(self, object: UUID) -> None: ...

    async def delete(self, object: T | UUID) -> None:
        if isinstance(object, UUID):
            query = sql_delete(self._model).where(self._model.id == object)
        else:
            query = sql_delete(self._model).where(self._model.id == object.id)
        _ = await self._session.execute(query)

    @overload
    async def get_by_id(self, object: T) -> T | None: ...
    @overload
    async def get_by_id(self, object: UUID) -> T | None: ...  # is needed for

    # avoiding struggles with getting files
    async def get_by_id(self, object: T | UUID) -> T | None:
        if isinstance(object, UUID):
            query = sql_select(self._model).where(self._model.id == object)
        else:
            query = sql_select(self._model).where(self._model.id == object.id)
        result = await self._session.execute(query)
        return result.scalars().first()

    async def get_all(self) -> Sequence[T] | None:
        query = sql_select(self._model)
        result = await self._session.execute(query)
        return result.scalars().all()

    async def get_by_custom_field(
        self, field_name: str, field_value: Any
    ) -> Sequence[T] | None:
        query = sql_select(self._model).where(
            getattr(self._model, field_name) == field_value
        )
        result = await self._session.execute(query)
        return result.scalars().all()

    async def check_exists(self, object_id: UUID) -> T | bool:
        query = sql_select(self._model).where(self._model.id == object_id)
        result = (await self._session.execute(query)).scalar()
        return result if result is not None else False
