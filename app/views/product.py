from flask import Blueprint, request
from app.models.product import db, Product
from app.models.serializer.product_schema import ProductSchema
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
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
def create_one_product():
    data = request.get_json()

    product = Product(
        name=data['name'],
        price=data['price'],
        description=data['description'],
        image=data['image']
    )

    try:
        db.session.add(product)
        db.session.commit()
        return build_api_response(HTTPStatus.CREATED)
    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)


@bp_products.route('/<int:product_id>', methods=['DELETE'])
def delete_one_product(product_id: int):
    Product.query.filter_by(id=product_id).delete()
    db.session.commit()

    return build_api_response(HTTPStatus.OK)


@bp_products.route('/<int:product_id>', methods=['PUT'])
def update_one_product(product_id: int):
    data = request.get_json()

    product = Product.query.get_or_404(product_id)

    product.name = data['name'] if data.get('name') else product.name
    product.price = data['price'] if data.get('price') else product.price
    product.description = data['description'] if data.get(
        'description') else product.description
    product.image = data['image'] if data.get('image') else product.image
