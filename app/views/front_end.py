from flask import Blueprint, request, render_template
from app.models import Category, Product
import json

bp_front_end = Blueprint('api_front_end', __name__, url_prefix='/')


@bp_front_end.route('', methods=['GET'])
def home():
    return render_template("home.html.jinja")


@bp_front_end.route('category_list', methods=['GET'])
def list_category():
    response = Category.query.all()
    category_list = [dict(id=category.id,name=category.name, link=f"category_list/{category.id}") for category in response]

    return render_template("category_list.html.jinja", data=category_list)


@bp_front_end.route('category_list/<int:category_id>', methods=['GET'])
def list_category_id(category_id):
    response = Product.query.filter_by(category_id=category_id)
    product_list = [dict(id=product.id, name=product.name, image=product.image, price=product.price) for product in response]

    return render_template("products_list.html.jinja", data=product_list)
