from fastapi import APIRouter

from .listing import router as listing_router

router = APIRouter()

router.include_router(listing_router, prefix="/listings", tags=["Listings"])
