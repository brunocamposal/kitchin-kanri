from environs import Env
from secrets import token_hex
from flask import Flask
from flask_jwt_extended import JWTManager

from app.views.orders import bp_orders
from app.views.product import bp_products
from app.views.front_end import bp_front_end
from app.views.categories import bp as bp_categories
from app.views.users import bp_users
from app.views.authenticator import bp_auth

from app.models import configure


def create_app():
    env = Env()
    env.read_env()

    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = env.bool(
        'SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config['SQLALCHEMY_DATABASE_URI'] = env.str('SQLALCHEMY_DATABASE_URI')
    app.config['JWT_SECRET_KEY'] = token_hex(16)

    # Configura db, ma e o migrate
    configure(app)

    # Instancia o JWT:
    JWTManager(app)

    # Chamada da view
    app.register_blueprint(bp_front_end)
    app.register_blueprint(bp_categories)
    app.register_blueprint(bp_products)
    app.register_blueprint(bp_orders)
    app.register_blueprint(bp_users)
    app.register_blueprint(bp_auth)

    return app
