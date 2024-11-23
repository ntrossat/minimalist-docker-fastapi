from datetime import datetime

from sqlmodel import SQLModel, Field


class ItemInput(SQLModel):
    name: str


class Item(ItemInput, table=True):
    id: int | None = Field(default=None, nullable=False, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())
