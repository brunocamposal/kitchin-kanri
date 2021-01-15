from flask import Flask
from environs import Env
from app.views.orders import bp_orders
from app.views.product import bp_products
from app.views.categories import bp_categories
from app.models import configure


def create_app():
    env = Env()
    env.read_env()

    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = env.bool(
        'SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config['SQLALCHEMY_DATABASE_URI'] = env.str('SQLALCHEMY_DATABASE_URI')

    ## Configura db, ma e o migrate
    configure(app)

    # Chamada da view
    app.register_blueprint(bp_categories)
    app.register_blueprint(bp_products)
    app.register_blueprint(bp_orders)

    return app
