from app.repositories.base_repository import BaseRepository
from app.models.item import Item


class ItemRepository(BaseRepository):
    model = Item
