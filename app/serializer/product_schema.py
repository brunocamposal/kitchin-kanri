from app.models import ma, Product


class ProductSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Product

    id = ma.auto_field()
    name = ma.auto_field()
    price = ma.auto_field()
    description = ma.auto_field()
    category_id = ma.auto_field()
