from flask import Blueprint, request
from app.services.category_services import category_list, update_category, delete_category, register_category
# /categories

bp_categories = Blueprint('categories', __name__)


@bp_categories.route('/categories', methods=['GET','POST'])
def categories():
    if request.method == 'POST':

        data = request.get_json()
        return register_category(data)
    return category_list()

# /categories<category_id>
@bp_categories.route('/categories/<int:category_id>', methods=['DELETE', 'PATCH'])
def category(category_id):
    if request.method == 'DELETE':
        return delete_category(category_id)
    
    data = request.get_json()
    
    return update_category(category_id, data)


