from flask.views import MethodView
from .items_repository import ItemModel, PlainItemSchema
from .items_service import ItemService
from flask_smorest import abort, Blueprint


blp = Blueprint("items", __name__, description="Operations on items")

@blp.route("/item")
class Location(MethodView):
    @blp.arguments(PlainItemSchema)
    @blp.response(200, PlainItemSchema)
    def post(self, item_data):
        item = ItemService.create(item_data)
        return item
    #
    # @blp.response(200, PlainLocationSchema(many=True))
    # def get(self):
    #     return LocationModel.query.all()
