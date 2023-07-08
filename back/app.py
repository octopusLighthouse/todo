from flask import Flask
from flask_smorest import Api
from .db import db
from dotenv import load_dotenv
from .config import app_config
from flask_migrate import Migrate
from .organization import OrganizationBlueprint
from .location import LocationBlueprint, LocationModel
from .item import ItemBlueprint, ItemModel
from .qrs import QRBlueprint
from .traindata import IntentsBlueprint, PatternBlueprint
from .utils import create_model
from .traindata import ResponseModel, ResponseBlueprint
from .traindata import greetings_responses, menu_responses, bestellen_responses
from .tag import TagBlueprint
from .category import CategoryBlueprint
def create_app():
    app = Flask(__name__)

    load_dotenv()
    app_config(app)

    db.init_app(app)
    migrate = Migrate(app, db, table='QRmenu/back/migrations')

    api = Api(app)

    api.register_blueprint(OrganizationBlueprint)
    api.register_blueprint(LocationBlueprint)
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(QRBlueprint)
    api.register_blueprint(IntentsBlueprint)
    api.register_blueprint(PatternBlueprint)
    api.register_blueprint(ResponseBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(CategoryBlueprint)








    return app
# app = create_app()
# with app.app_context():
#     for response in bestellen_responses:
#         response_data = {
#             "response": response,
#             "intent_id": 24,
#             "language": "NL"
#         }
#         create_model(ResponseModel, response_data)
# app = create_app()
# with app.app_context():
#     location_id = '28f1b95a19d44b478dda48eb43ae3426'
#     query = db.session.query(ItemModel).join(LocationModel).filter(LocationModel.id == location_id)
#
#     # Execute the query and retrieve the items
#     items = query.all()
#
#     # Process the queried items
#     for item in items:
#         # Access the item data
#         item_id = item.id
#         item_name = item.name
#         # ... other item attributes
#         print(f"Item ID: {item_id}, Item Name: {item_name}")