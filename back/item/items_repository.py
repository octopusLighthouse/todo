from ..common_imports import *

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4().hex))
    name = db.Column(db.String(120), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    created_at = db.Column("createdAt", db.DateTime, default=datetime.now)
    location_id = db.Column("locationId", db.String, db.ForeignKey("locations.id"), nullable=False)
    location = db.relationship("LocationModel", back_populates="items")

class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    created_at = fields.Str(data_key='createdAt', attribute='created_at', dump_only=True)
    location_id = fields.Str(data_key='locationId', attribute='location_id', required=True)


class ItemSchema(PlainItemSchema):
    pass
