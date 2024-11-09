from datetime import datetime
from typing import List


from sqlmodel import SQLModel, Field, select, UniqueConstraint
from sqlmodel.ext.asyncio.session import AsyncSession


class ItemCreate(SQLModel):
    name: str


class ItemModel(ItemCreate):
    id: int | None = Field(default=None, nullable=False, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())


class Item(ItemModel, table=True):

    @staticmethod
    async def get_all(session: AsyncSession) -> list[ItemModel]:
        response = await session.exec(select(Item))
        return response.all()

    @staticmethod
    async def get_by_id(id: int, session: AsyncSession) -> ItemModel | None:
        item = await session.get(Item, id)
        return item

    @staticmethod
    async def create(item: ItemModel, session: AsyncSession) -> ItemModel:
        item = Item.model_validate(item)
        session.add(item)
        await session.commit()
        await session.refresh(item)
        return item

    @staticmethod
    async def update(
        item: ItemModel, update: ItemModel, session: AsyncSession
    ) -> ItemModel:
        update_data = Item.model_validate(update)
        item.sqlmodel_update(update_data)
        session.add(item)
        await session.commit()
        await session.refresh(item)
        return item

    @staticmethod
    async def delete(item: ItemModel, session: AsyncSession) -> None:
        await session.delete(item)
        await session.commit()
