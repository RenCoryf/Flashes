from sqlalchemy.ext.asyncio import AsyncSession

from ..models.tables import Card as card_table
from .base import Base


class Card(Base[card_table]):
    def __init__(self, session: AsyncSession):
        super().__init__(card_table, session)
