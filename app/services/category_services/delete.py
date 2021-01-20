from app.services.http import build_api_response

from app.models import Category
from flask import current_app
from http import HTTPStatus

def delete_category(category_id: int):

    category = Category.query.filter_by(id=category_id).first()

    if category is None:
        return build_api_response(404)

    current_app.db.session.delete(category)
    current_app.db.session.commit()

    return build_api_response(202)