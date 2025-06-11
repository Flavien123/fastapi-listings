from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from collections.abc import AsyncGenerator

from core.config import settings


engine = create_async_engine(settings.db_url)

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

