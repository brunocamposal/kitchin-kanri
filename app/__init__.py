from flask import Flask
from app.models import db
from environs import Env


def create_app():
    env = Env()
    env.read_env()
        
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = env.bool('SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config['SQLALCHEMY_DATABASE_URI'] = env.str('SQLALCHEMY_DATABASE_URI')

    db.init_app(app)

    ## Chamada da view
    ## app.register_blueprint(bp_categories)

    return app
