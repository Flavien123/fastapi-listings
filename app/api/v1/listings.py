from typing import Dict, Any

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException, status

from crud.crud import CrudBase
from models.listings import Listings
from database import database
from schemas.listings import ListingResponse, ListingCreate


listing_crud = CrudBase(Listings)

router = APIRouter()


@router.get("/", response_model=list[ListingResponse])
async def get_listings(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(database.get_db)
):
    result = await listing_crud.get_many(db, skip=skip, limit=limit)
    return result


@router.get("/{listing_id}", response_model=ListingResponse)
async def get_listing(listing_id: int, db: AsyncSession = Depends(database.get_db)):
    result = await listing_crud.get_by_id(db, listing_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Listing was not found"
        )
    return result


@router.post("/", response_model=ListingResponse, status_code=status.HTTP_201_CREATED)
async def create_listing(
    listing_data: ListingCreate, db: AsyncSession = Depends(database.get_db)
):
    result = await listing_crud.create(db, listing_data.model_dump())
    return result


@router.patch("/{listing_id}", response_model=ListingResponse)
async def update_listing_partial(
    listing_id: int,
    listing_data: Dict[str, Any],
    db: AsyncSession = Depends(database.get_db),
):
    result = await listing_crud.update_by_id(db, listing_id, listing_data)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Listing was not found"
        )
    return result


@router.put("/{listing_id}", response_model=ListingResponse)
async def update_listing_full(
    listing_id: int,
    listing_data: ListingCreate,
    db: AsyncSession = Depends(database.get_db),
):
    result = await listing_crud.update_by_id(db, listing_id, listing_data.model_dump())
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Listing was not found"
        )
    return result


@router.delete("/{listing_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_listing(listing_id: int, db: AsyncSession = Depends(database.get_db)):
    result = await listing_crud.delete_by_id(db, listing_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Listing was not found"
        )
    return
