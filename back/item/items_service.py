from .items_repository import ItemModel
from ..utils import create_model


class ItemService:
    @staticmethod
    def create(data):
        return create_model(ItemModel, data)