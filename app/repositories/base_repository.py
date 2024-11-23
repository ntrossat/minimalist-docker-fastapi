from sqlmodel import SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession


class BaseRepository:
    model = SQLModel

    @classmethod
    async def list(cls, session: AsyncSession) -> list[model]:
        response = await session.exec(select(cls.model))
        return response.all()

    @classmethod
    async def get(cls, session: AsyncSession, id: int) -> model:
        item = await session.get(cls.model, id)
        return item

    @classmethod
    async def save(cls, session: AsyncSession, item: model) -> model:
        session.add(item)
        await session.commit()
        await session.refresh(item)
        return item

    @classmethod
    async def delete(cls, session: AsyncSession, item: model) -> None:
        await session.delete(item)
        await session.commit()
        return None
