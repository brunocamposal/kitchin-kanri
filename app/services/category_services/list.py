from app.models.category import Category
from app.serializer.category_schema import categories_schema

def category_list():
    return categories_schema.jsonify(Category.query.all())