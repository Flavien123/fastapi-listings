from typing import TypeVar, Generic, Type, Optional, Dict, Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import Base

ModelType = TypeVar("ModelType", bound=Base)


class CrudBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get_many(
        self, db: AsyncSession, skip: int = 0, limit: int = 100
    ) -> list[ModelType]:
        result = await db.execute(select(self.model).offset(skip).limit(limit))
        return list(result.scalars().all())

    async def get_by_id(self, db: AsyncSession, obj_id: int) -> Optional[ModelType]:
        result = await db.execute(select(self.model).filter(self.model.id == obj_id))
        return result.scalar_one_or_none()

    async def create(self, db: AsyncSession, obj_in: dict):
        db_obj = self.model(**obj_in)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update_by_id(
        self, db: AsyncSession, obj_id: int, obj_in: Dict[str, Any]
    ) -> Optional[ModelType]:
        db_obj = await self.get_by_id(db, obj_id)
        if not db_obj:
            return None

        for field, value in obj_in.items():
            if hasattr(db_obj, field):
                setattr(db_obj, field, value)

        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def delete_by_id(self, db: AsyncSession, obj_id: int) -> Optional[ModelType]:
        db_obj = await self.get_by_id(db, obj_id)
        if not db_obj:
            return None

        await db.delete(db_obj)
        await db.commit()
        return db_obj
