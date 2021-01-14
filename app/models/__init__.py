from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

# Tabelas

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=False, nullable=True)
    payment_method = db.Column(db.String(120), unique=False, nullable=False)
    total_price = db.Column(db.Float, unique=False, nullable=False)

    product = db.relationship("Product", secondary=order_list, back_populates='products')
    
    def __repr__(self):
        return f'<Order {self.date} - #{self.order_id}: {self.status} >'


