from app.models import Category
from app.serializer.category_schema import category_schema
from app.services.http import build_api_response

def get_category(category_id):
    category =  Category.query.filter_by(id=category_id).first()
    if category is None:
        return build_api_response(404)
    return build_api_response(200, category_schema.dumps(category))