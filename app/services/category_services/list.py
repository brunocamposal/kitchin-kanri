from app.models import Category
from app.serializer.category_schema import categories_schema
from http import HTTPStatus

def category_list():
    return categories_schema.jsonify(Category.query.all()), HTTPStatus.OK