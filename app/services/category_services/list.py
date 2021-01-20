from app.models import Category
from app.serializer.category_schema import categories_schema
from app.services.http import build_api_response

def category_list():
    categories =  Category.query.all()
    return build_api_response(200, categories_schema.dumps(categories))