from app.serializer.category_schema import category_schema
from app.services.http import build_api_response
from app.models import Category
from flask import current_app
from http import HTTPStatus
from typing import Dict


def update_category(category_id: int , data: Dict):

    category = Category.query.filter_by(id=category_id).first()

    if category is None:
        return build_api_response(404)

    setattr(category, 'name', data['name'])

    current_app.db.session.commit()

    return build_api_response(200, category_schema.dumps(category))
    