import uuid

from sqlmodel import SQLModel, Field


class ItemInput(SQLModel):
    name: str


class Item(ItemInput, table=True):
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)