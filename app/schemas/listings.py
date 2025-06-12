from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field


class ListingsBase(BaseModel):
    title: str = Field(
        examples=["Cozy apartment in the city center"],
        description="Listing title, up to 200 characters.",
    )
    discription: str = Field(
        examples=[
            "Spacious apartment with new renovation and park views. All infrastructure nearby."
        ],
        description="Detailed listing description, up to 1000 characters.",
    )
    price: int = Field(examples=[15000000], description="Price of the object.")
    city: str = Field(
        examples=["New-York"], description="City where the object is located."
    )


class ListingResponse(ListingsBase):
    id: int = Field(examples=[1], description="Unique listing identifier.")
    created_at: datetime = Field(
        examples=[datetime.now()], description="Date and time of listing creation."
    )
    title: str
    discription: str
    price: int
    city: str

    class Config:
        from_attributes = True


class ListingCreate(ListingsBase):
    pass


class ListingUpdate(ListingsBase):
    title: Optional[str] = Field(
        None,
        examples=["Updated title"],
        description="New listing title (optional).",
    )
    discription: Optional[str] = Field(
        None,
        examples=["Updated description with new details."],
        description="New listing description (optional).",
    )
    price: Optional[int] = Field(
        None, examples=[16000000], description="New object price (optional)."
    )
    city: Optional[str] = Field(
        None,
        examples=["Berlin"],
        description="New city for the object (optional).",
    )


