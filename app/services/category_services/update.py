from app.serializer.category_schema import category_schema
from app.models.category import Category
from flask import current_app
from typing import Dict


def update_category(category_id: int , data: Dict):

    category = Category.query.get_or_404(category_id)

    setattr(category, 'name', data['name'])

    current_app.db.session.commit()

    return category_schema.jsonify(category)