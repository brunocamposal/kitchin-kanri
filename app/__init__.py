from flask import Flask
from app.models import mg, db
from environs import Env
from app.views.orders import bp_orders
from app.views.product import bp_products


def create_app():
    env = Env()
    env.read_env()

    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = env.bool(
        'SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config['SQLALCHEMY_DATABASE_URI'] = env.str('SQLALCHEMY_DATABASE_URI')

    db.init_app(app)
    mg.init_app(app, db)

    # Chamada da view
    app.register_blueprint(bp_products)
    app.register_blueprint(bp_orders)

    return app
