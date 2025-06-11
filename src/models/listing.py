from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, func

from typing import Optional

from db.base import Base

class Listing(Base):
    __tablename__ = "listings"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[Optional[str]] = mapped_column(String(1000))
    price: Mapped[int] = mapped_column()
    city: Mapped[str] = mapped_column(String(200))
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())