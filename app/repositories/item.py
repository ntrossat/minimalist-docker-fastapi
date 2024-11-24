from app.repositories.base_repository import BaseRepository
from app.models import Item


class ItemRepository(BaseRepository):
    model = Item
