from flask import Blueprint, request
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from app.services.http import build_api_response

bp_products = Blueprint('api_products', __name__, url_prefix='/products')


@bp_products.route('/')
