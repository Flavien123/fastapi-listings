from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from core import settings
from database import Base


class Database:
    def __init__(self, url: str, echo: bool):
        self.engine: AsyncEngine = create_async_engine(url=url, echo=echo)
        self.session: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine, autoflush=False, expire_on_commit=False
        )

    async def get_db(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session() as session:
            yield session

    async def init_models(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


database = Database(url=settings.db.db_url, echo=settings.db.db_echo)
