from fastapi import APIRouter

from api.v1.listings import router as listings_router

router = APIRouter()

router.include_router(listings_router, prefix="/listings", tags=["Listings"])
