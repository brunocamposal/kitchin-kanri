from flask import Blueprint, request


# /categories

bp = Blueprint('categories', __name__)


@bp.route('/categories', methods=['GET','POST'])
def categories():
    if request.method == 'POST':
        return register_category()
    return category_list()

# /categories<category_id>
@bp.route('/categories/<category_id>', methods=['DELETE', 'PATCH'])
def category(category_id):
    if request.method == 'DELETE':
        return delete_category(category_id)
    
    return update_category(category_id)


