from flask import Blueprint, request
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from app.services.http import build_api_response

bp_products = Blueprint('api_products', __name__, url_prefix='/products')


@bp_products.route('/')
def list_all():
    pass


@bp_products.route('/<int:product_id>')
def list_one_product():
    pass


@bp_products.route('/', methods=['POST'])
def create_one_product():
    pass


@bp_products.route('/<int:product_id>', methods=['DELETE'])
def delete_one_product(user_id: int):
    pass


@bp_products.route('/<int:product_id>', methods=['PUT'])
def update_one_product(user_id: int):
    pass
