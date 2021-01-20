from app.serializer.category_schema import category_schema
from app.services.http import build_api_response
from app.models import Category
from flask import current_app
from http import HTTPStatus
from typing import Dict


def update_category(category_id: int , data: Dict):

    category = Category.query.get_or_404(category_id)

    if category == None:
        return build_api_response(404)

    setattr(category, 'name', data['name'])

    current_app.db.session.commit()

    return category_schema.jsonify(category), HTTPStatus.OK