from fastapi import APIRouter, HTTPException, Depends

from core.postgres.db import get_session, AsyncSession
from app.models.item import Item, ItemInput
from app.models.response import MessageResponse
from app.repositories.item import ItemRepository

router = APIRouter()


@router.get("/", response_model=list[Item])
async def get_items(
    repository: ItemRepository = Depends(get_session),
    session: AsyncSession = Depends(get_session),
) -> list[Item]:
    """Get all items."""
    return await ItemRepository.list(session)


@router.get("/{id}", response_model=Item)
async def get_item(
    id: int,
    session: AsyncSession = Depends(get_session),
) -> Item:
    """Get item by ID."""
    item = await ItemRepository.get(session, id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/", response_model=Item, status_code=201)
async def create_item(
    item: ItemInput, session: AsyncSession = Depends(get_session)
) -> Item:
    """Create a new item."""
    item = Item.model_validate(item)
    return await ItemRepository.save(session, item)


# TODO Fix Timestamp issue
@router.put("/{id}", response_model=Item)
async def update_item(
    id: int,
    item: ItemInput,
    session: AsyncSession = Depends(get_session),
) -> Item:
    """
    Update an existing item.
    """
    item_db = await ItemRepository.get(session, id)

    if not item_db:
        raise HTTPException(status_code=404, detail="Item not found")

    item = Item.model_validate(item)
    item.id = id
    item_db.sqlmodel_update(item)

    return await ItemRepository.save(session, item_db)


@router.delete("/{id}")
async def delete_item(
    id: int,
    session: AsyncSession = Depends(get_session),
) -> MessageResponse:
    """
    Delete an item.
    """
    item = await ItemRepository.get(session, id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    await ItemRepository.delete(session, item)
    return MessageResponse(message="Item deleted successfully")
