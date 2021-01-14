from app.models import Order, ma
from app.models.serializer.product_schema import ProductSchema


class OrderSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Order

    id = ma.auto_field()
    status = ma.auto_field()
    date = ma.auto_field()
    payment_method = ma.auto_field()
    total_price = ma.auto_field()
    products_id = fields.Nested(ProductSchema, many=True)
