from app.serializer.category_schema import category_schema
from app.models import Category
from flask import current_app
from http import HTTPStatus
from typing import Dict


def update_category(category_id: int , data: Dict):

    category = Category.query.get_or_404(category_id)

    setattr(category, 'name', data['name'])

    current_app.db.session.commit()

    return category_schema.jsonify(category), HTTPStatus.OK