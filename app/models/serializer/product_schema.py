
from models.product import Product, ma


class ProductSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Product

    id = ma.auto_field()
    name = ma.auto_field()
    price = ma.auto_field()
    description = ma.auto_field()
    orders = fields.Nested(OrderSchema, many=True)
