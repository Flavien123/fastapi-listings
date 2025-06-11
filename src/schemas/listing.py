from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ListingBase(BaseModel):
    title: str = Field(example="Просторная квартира")
    description: Optional[str] = Field(None, example="2км квартира, 6 этаж")
    price: int = Field(gt=0, example=1_000_000)
    city: str = Field(example="Астана")

class ListingCreate(ListingBase):
    pass

class ListingUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    city: Optional[str] = None

class ListingResponse(ListingBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
