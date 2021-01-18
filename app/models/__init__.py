from marshmallow import fields
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()


def configure(app):
    db.init_app(app)
    ma.init_app(app)
    app.db = db
    Migrate(app, app.db)

# Tabelas


product_list = db.Table(
    'product_list',
    db.Column('order_id', db.Integer, db.ForeignKey(
        'order.id')),
    db.Column('product_id', db.Integer, db.ForeignKey(
        'product.id'))
)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=False, nullable=True)
    total_price = db.Column(db.Float, unique=False, nullable=True)
    payment_method = db.Column(db.String(120), unique=False, nullable=True)

    products = db.relationship(
        "Product", secondary=product_list, back_populates='orders')

    def __repr__(self):
        return f'<Order {self.date} - #{self.order_id}: {self.status} >'


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(999), nullable=False)
    image = db.Column(db.String(256), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    orders = db.relationship(
        "Order", secondary=product_list, back_populates="products")


class User(db.Model):
    """ User table, with option to give admin attr to some """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)
