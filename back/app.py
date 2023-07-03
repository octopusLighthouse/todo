from flask import Flask
from flask_smorest import Api
from .db import db
from dotenv import load_dotenv
from .config import app_config
from flask_migrate import Migrate
from .organization import OrganizationBlueprint
from .location import LocationBlueprint
from .item import ItemBlueprint
from .qrs import QRBlueprint

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



    return app
