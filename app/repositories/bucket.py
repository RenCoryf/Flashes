from sqlalchemy.ext.asyncio import AsyncSession

from ..models.tables import Bucket as bucket_table
from .base import BaseRepo


class Bucket(BaseRepo[bucket_table]):
    def __init__(self, session: AsyncSession):
        super().__init__(bucket_table, session)
