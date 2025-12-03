from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.Config import config


class Database:
    def __init__(self):
        self.url = self._make_url(
            user=config.POSTGRES_USER,
            password=config.POSTGRES_PASSWORD,
            db_name=config.POSTGRES_DB,
            host=config.POSTGRES_HOST,
            port=config.POSTGRES_PORT,
        )
        self.engine = create_async_engine(self.url, echo=False, future=True)
        self._async_sessionmaker = async_sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession
        )

    @asynccontextmanager
    async def sessionmaker(self):
        async with self._async_sessionmaker() as session:
            try:
                yield session
            except Exception:
                await session.rollback()
                raise
            else:
                await session.commit()

    def _make_url(
        self, user: str, password: str, db_name: str, host: str, port: str
    ) -> str:
        return f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}"
