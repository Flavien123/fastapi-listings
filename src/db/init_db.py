import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from models.listing import Base

db_url = "sqlite+aiosqlite:///./db.sqlite3"
engine = create_async_engine(db_url, echo=True)

async def init_db():
    async with engine.begin() as conn:
        # Убедимся, что drop_all и create_all работают:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_db())
