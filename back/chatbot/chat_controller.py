from flask.views import MethodView
from flask_smorest import abort, Blueprint
from ..item import ItemModel, PlainItemSchema
from .chat_service import ChatbotService


blp = Blueprint("chats", __name__, description="Operations on chats")

@blp.route("/chat/<string:location_id>")
class Chat(MethodView):
    #@blp.response(200, PlainItemSchema(many=True))

    def post(self, location_id, user_input=None):

        location_items = ItemModel.query.filter(ItemModel.location_id == location_id)
        chat = ChatbotService(location_items)
        return chat.menu

