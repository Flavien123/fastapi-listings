from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field


class ListingsBase(BaseModel):
    title: str = Field(
        examples=["Уютная квартира в центре"],
        description="Заголовок объявления, до 200 символов.",
    )
    discription: str = Field(
        examples=[
            "Просторная квартира с новым ремонтом и видом на парк. Рядом вся инфраструктура."
        ],
        description="Подробное описание объявления, до 1000 символов.",
    )
    price: int = Field(examples=[15000000], description="Цена объекта в тенге.")
    city: str = Field(
        examples=["Астана"], description="Город, в котором находится объект."
    )


class ListingResponse(ListingsBase):
    id: int = Field(examples=[1], description="Уникальный идентификатор объявления.")
    created_at: datetime = Field(
        examples=[datetime.now()], description="Дата и время создания объявления."
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
        examples=["Обновленный заголовок"],
        description="Новый заголовок объявления (необязательно).",
    )
    discription: Optional[str] = Field(
        None,
        examples=["Обновленное описание с новыми деталями."],
        description="Новое описание объявления (необязательно).",
    )
    price: Optional[int] = Field(
        None, examples=[16000000], description="Новая цена объекта (необязательно)."
    )
    city: Optional[str] = Field(
        None,
        examples=["Алматы"],
        description="Новый город для объекта (необязательно).",
    )
