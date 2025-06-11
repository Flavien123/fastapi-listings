from fastapi import APIRouter

from .listing import router as listing_router

router = APIRouter(prefix="/v1")

router.include_router(listing_router)