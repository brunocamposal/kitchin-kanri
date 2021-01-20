from app.models import Category
from app.serializer.category_schema import category_schema
from flask import current_app
from http import HTTPStatus
from typing import Dict

def register_category(data: Dict):

    category = Category(name=data['name'])

    current_app.db.session.add(category)
    current_app.db.session.commit()

    return category_schema.jsonify(category), HTTPStatus.CREATED