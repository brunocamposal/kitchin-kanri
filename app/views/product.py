from flask import Blueprint, request
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required

from app.models import db, Product
from app.serializer.product_schema import ProductSchema
from app.services.http import build_api_response


bp_products = Blueprint('api_products', __name__, url_prefix='/products')


@bp_products.route('')
def list_all():
    products = Product.query.all()

    return {
        'data': ProductSchema(many=True).dump(products)
    }, HTTPStatus.OK


@bp_products.route('/<int:product_id>')
def list_one_product(product_id: int):
    product = Product.query.get(product_id)

    if not product:
        return build_api_response(HTTPStatus.NOT_FOUND)

    return {
        'data': ProductSchema().dump(product)
    }


@bp_products.route('', methods=['POST'])
@jwt_required
def create_one_product():
    data = request.get_json()

    if not data:
        return build_api_response(HTTPStatus.NOT_FOUND)

    product = Product(
        name=data['name'],
        price=data['price'],
        description=data['description'],
        image=data['image'],
        category_id=data['category_id']
    )

    try:
        db.session.add(product)
        db.session.commit()
        return build_api_response(HTTPStatus.CREATED)
    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)


@bp_products.route('/<int:product_id>', methods=['DELETE'])
@jwt_required
def delete_one_product(product_id: int):

    product = Product.query.filter_by(id=product_id).first()

    if product is None:
        return build_api_response(HTTPStatus.NOT_FOUND)

    db.session.delete(product)
    db.session.commit()

    return build_api_response(HTTPStatus.OK)


@bp_products.route('/<int:product_id>', methods=['PUT'])
@jwt_required
def update_one_product(product_id: int):
    data = request.get_json()

    product = Product.query.get_or_404(product_id)

    if product is None:
        return build_api_response(HTTPStatus.NOT_FOUND)

    product.name = data['name'] if data.get('name') else product.name
    product.price = data['price'] if data.get('price') else product.price
    product.description = data['description'] if data.get(
        'description') else product.description
    product.category_id = data['category_id'] if data.get(
        'category_id') else product.category_id
    product.image = data['image'] if data.get(
        'image') else product.image


    print(product.image)
    db.session.commit()

    return {
        'data': ProductSchema().dump(product)
    }
