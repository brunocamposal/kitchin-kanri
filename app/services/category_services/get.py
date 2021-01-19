from app.models import Category
from app.serializer.category_schema import category_schema

def get_category(category_id):
    return category_schema.jsonify(Category.query.get_or_404(category_id))