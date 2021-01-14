from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from marshmallow import fields

db = SQLAlchemy()
mg = Migrate()
ma = Marshmallow()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    price = db.Column(db.Float(128), nullable=False)
    description = db.Column(db.String(999), nullable=False)
    image = db.Column(db.String(256), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    orders = db.relationship(
        "Order", secondary=product_list, back_populates="products")


class ProductSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Product

    id = ma.auto_field()
    name = ma.auto_field()
    price = ma.auto_field()
    description = ma.auto_field()
    orders = fields.Nested(OrderSchema, many=True)
