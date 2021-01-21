from app.services.category_services import category_list, update_category, delete_category, register_category

from flask_jwt_extended import jwt_optional, jwt_required, get_jwt_identity
from http import HTTPStatus
from app.services.category_services import get_category
from app.services.http import build_api_response
from flask import Blueprint, request, make_response
# /categories

bp = Blueprint('categories', __name__)


@bp_categories.route('/categories', methods=['GET', 'POST'])
@jwt_optional
def categories():

    if request.method == 'POST':

        user_identity = get_jwt_identity()

        if user_identity is not None:

            data = request.get_json(force=True)
            return register_category(data)

        return build_api_response(HTTPStatus.UNAUTHORIZED)

    return category_list()

  
@bp_categories.route('/categories/<int:category_id>', methods=['DELETE', 'PATCH'])
@jwt_required
def category(category_id):
    if request.method == 'DELETE':
        return delete_category(category_id)

    if request.method == 'PATCH':
        data = request.get_json()
    
        return update_category(category_id, data)

    data = request.get_json()
    return update_category(category_id, data)