from app.services.category_services import category_list, update_category, delete_category, register_category
from app.services.category_services import get_category
from app.services.http import build_api_response
from flask import Blueprint, request, make_response
# /categories

bp = Blueprint('categories', __name__)


##todo
## fazer um tratamento de erro se não ouver o id

@bp.route('/categories', methods=['GET','POST'])
def categories():
    if request.method == 'POST':

        data = request.get_json()
        return register_category(data)
    return category_list()

# /categories<category_id>
@bp.route('/categories/<int:category_id>', methods=['GET', 'DELETE', 'PATCH'])
def category(category_id):
    if request.method == 'DELETE':
        return delete_category(category_id)
    

    if request.method == 'PATCH':
        data = request.get_json()
    
        return update_category(category_id, data)


    return get_category(category_id)
  