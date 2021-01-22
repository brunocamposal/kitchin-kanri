from app.serializer.category_schema import category_schema
from app.services.http import build_api_response
from app.models import Category

def get_category(category_id):
    category =  Category.query.filter_by(id=category_id).first()

    if category == None:
        return build_api_response(404)
    
    return category_schema.jsonify(category)