from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()
mg = Migrate()

# Tabelas

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=False, nullable=True)
    total_price = db.Column(db.Float, unique=False, nullable=True)
    payment_method = db.Column(db.String(120), unique=False, nullable=True)

    ##payment_method_id = db.Column(db.Integer, db.ForeignKey('paymentmethod.id'))
    
    ##payment_method = db.relationship("PaymentMethod", back_populates="orders")

    ##product = db.relationship("Product", secondary=order_list, back_populates='products')
    
    def __repr__(self):
        return f'<Order {self.date} - #{self.order_id}: {self.status} >'


class PaymentMethod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
   
    ##orders = db.relationship("Order", back_populates="payment_method")

    def __repr__(self):
        return f'<PaymentMethod {self.id}: {self.name} >'
