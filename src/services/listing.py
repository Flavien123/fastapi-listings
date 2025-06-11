from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models.listing import Listing
from schemas.listing import ListingCreate

async def get_listing_by_id(listing_id: int, db: AsyncSession) -> Listing | None:
    result = await db.execute(select(Listing).where(Listing.id == listing_id))
    listing = result.scalar_one_or_none()
    return listing

async def get_all_listings(db: AsyncSession):
    result = await db.execute(select(Listing))
    listings = result.scalars().all()
    return listings

async def create_new_listing(listing_data: ListingCreate, db: AsyncSession) -> Listing:
    listing = Listing(**listing_data.dict())
    db.add(listing)
    await db.commit()
    await db.refresh(listing)
    return listing

async def update_listing_by_id():
    pass

async def delete_listing_by_id(listing_id: int, db: AsyncSession):
    result = await db.execute(select(Listing).where(Listing.id == listing_id))
    listing = result.scalar_one_or_none()
    if not listing:
        return False
    await db.delete(listing)
    await db.commit()
    return True