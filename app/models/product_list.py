from app.models import db

product_list = db.Table('product_list',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id', primary_key=True))
)