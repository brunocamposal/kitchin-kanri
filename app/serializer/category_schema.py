from app.models import Category, ma

class CategorySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Category

    id = ma.auto_field()
    name = ma.auto_field()


category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)
