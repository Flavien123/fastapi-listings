from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException, status, Depends

from schemas.listing import ListingResponse, ListingCreate
from services.listing import get_listing_by_id, get_all_listings, create_new_listing, delete_listing_by_id, update_listing_by_id

from db.session import get_db

router = APIRouter()

@router.get("/{listing_id}", response_model=ListingResponse)
async def get_listing(listing_id: int, db: AsyncSession = Depends(get_db)):
    listing = await get_listing_by_id(listing_id, db)
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    return listing

@router.get("/", response_model=list[ListingResponse])
async def get_listings(db: AsyncSession = Depends(get_db)):
    listings = await get_all_listings(db)
    if not listings:
        raise HTTPException(status_code=404, detail="Listings not found")
    return listings

@router.post("/", response_model=ListingResponse, status_code=status.HTTP_201_CREATED)
async def create_listing(listing_data: ListingCreate, db: AsyncSession = Depends(get_db)):
    return await create_new_listing(listing_data, db)

@router.put("/{listing_id}", response_model=ListingResponse)
async def update_listing():
    pass

@router.delete("/{listing_id}")
async def delete_listing(listing_id: int, db: AsyncSession = Depends(get_db)):
   result = await delete_listing_by_id(listing_id, db)
   return result