from app.models import Category
from app.services.http import build_api_response
from flask import current_app
from http import HTTPStatus

def delete_category(category_id: int):

    category = Category.query.get_or_404(category_id)

    current_app.db.session.delete(category)
    current_app.db.session.commit()

    return {'message': 'Deleted'}, HTTPStatus.OK