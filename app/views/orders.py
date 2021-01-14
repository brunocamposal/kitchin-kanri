from flask import Blueprint, request
from app.models import db, Order
from app.models.serializer.order_schema import OrderSchema
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from app.services.http import build_api_response


bp_orders = Blueprint('api_orders', __name__, url_prefix='/orders')


@bp_orders.route('', methods=['POST'])
def create():
    data = request.get_json()
    order = Order(
        status=data["status"],
        date=data['date'],
        payment_method=data['payment_method']
    )

    try:
        db.session.add(order)
        db.session.commit()
        return build_api_response(HTTPStatus.CREATED)
    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)


@bp_orders.route('', methods=['GET'])
def get():
    orders = Order.query.all()

    return {
        'data': OrderSchema(many=True).dump(orders)
    }, HTTPStatus.OK


@bp_orders.route('/<order_id>', methods=['GET'])
def get_id(order_id: int):

    order = Order.query.filter(Order.id == order_id).all()

    if not order:
        return build_api_response(HTTPStatus.NOT_FOUND)

    return {'data': OrderSchema(many=True).dump(order)}


@bp_orders.route('/<order_id>', methods=['PUT'])
def put(order_id: int):

    data = request.get_json()

    order = Order.query.get_or_404(order_id)

    order.status = data['status'] if data.get('status') else order.status

    db.session.commit()
    return {'data': OrderSchema().dump(order)}


@bp_orders.route('/<order_id>', methods=['DELETE'])
def delete(order_id: int):

    order = Order.query.filter_by(id=order_id).delete()

    if not order:
        return build_api_response(HTTPStatus.NOT_FOUND)

    db.session.commit()
    return build_api_response(HTTPStatus.OK)
