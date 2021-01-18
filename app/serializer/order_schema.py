from app.models import ma, Order
from app.serializer.product_schema import ProductSchema
from marshmallow import fields


class OrderSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Order

    id = ma.auto_field()
    status = ma.auto_field()
    date = ma.auto_field()
    payment_method = ma.auto_field()
    total_price = ma.auto_field()
    products_id = fields.Nested(ProductSchema, many=True)
