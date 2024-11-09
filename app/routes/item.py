from datetime import datetime
from typing import List, Any

from fastapi import APIRouter, HTTPException, Depends

from core.postgres.db import get_session, AsyncSession
from app.models.item import Item, ItemCreate
from app.models.response import MessageResponse

router = APIRouter()


@router.get("/", response_model=List[Item])
async def get_items(
    session: AsyncSession = Depends(get_session),
) -> List[Item]:
    """Get all items."""
    return await Item.get_all(session)


@router.get("/{id}", response_model=Item)
async def get_item(
    id: int,
    session: AsyncSession = Depends(get_session),
) -> List[Item]:
    """Get item by ID."""
    item = await Item.get_by_id(id, session)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/", response_model=Item, status_code=201)
async def create_item(
    item: ItemCreate, session: AsyncSession = Depends(get_session)
) -> Item:
    """Create a new item."""
    return await Item.create(item, session)


@router.put("/{id}", response_model=Item)
async def update_item(
    id: int,
    update: Item,
    session: AsyncSession = Depends(get_session),
) -> Item:
    """
    Update an existing item.
    """
    item = await Item.get_by_id(id, session)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return await Item.update(item, update, session)


@router.delete("/{id}")
async def delete_item(
    id: int,
    session: AsyncSession = Depends(get_session),
) -> MessageResponse:
    """
    Delete an item.
    """
    item = await Item.get_by_id(id, session)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    await Item.delete(item, session)
    return MessageResponse(message="Item deleted successfully")
