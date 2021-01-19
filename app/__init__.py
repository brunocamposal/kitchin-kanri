from flask import Flask
from app.models import configure
from environs import Env
from app.views.orders import bp_orders
from app.views.product import bp_products
from app.views.category_view import bp as bp_category



def create_app():
    env = Env()
    env.read_env()

    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = env.bool(
        'SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config['SQLALCHEMY_DATABASE_URI'] = env.str('SQLALCHEMY_DATABASE_URI')

    configure(app)
    # Chamada da view
    app.register_blueprint(bp_products)
    app.register_blueprint(bp_orders)
    app.register_blueprint(bp_category)

    return app
