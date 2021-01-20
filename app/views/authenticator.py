from datetime import timedelta
from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_refresh_token_required
from http import HTTPStatus

from app.models import User, db
from app.services.http import build_api_response


bp_auth = Blueprint("bp_auth", __name__, url_prefix="/authentication")

# encriptar senha com biblioteca do python
# melhorar mensagem de user já existente


@bp_auth.route('/signup', methods=['POST'])
def signup():

    data = request.get_json(force=True)

    user = User(
        name=data.get('name', None),
        email=data.get('email', None),
        password=data.get('password', None),
        is_admin=data.get('is_admin', None)
    )

    try:
        db.session.add(user)
        db.session.commit()

        return build_api_response(HTTPStatus.CREATED)

    except IntegrityError:
        return build_api_response(HTTPStatus.UNPROCESSABLE_ENTITY)


@bp_auth.route('/login', methods=['POST'])
def login():

    user_found = User.query.filter_by(
        email=request.get_json(force=True).get('email')).first()

    pwd_informed = user_found.password
    pwd_db = request.get_json(force=True).get('pwd')

    if pwd_informed != pwd_db:

        return build_api_response(HTTPStatus.UNAUTHORIZED)

    access_token = create_access_token(
        identity=user_found.id, expires_delta=timedelta(days=5))

    fresh_token = create_refresh_token(
        identity=user_found.id, expires_delta=timedelta(days=10))

    return {'data': {
        'name': user_found.name,
        'email': user_found.email,
        'is_admin': user_found.is_admin,
        'access_token': access_token,
        'fresh_token': fresh_token
    }}


@bp_auth.route('/fresh_token', methods=['GET'])
@jwt_refresh_token_required
def get_fresh_token():

    user_id = get_jwt_identity()
    print(user_id)
    access_token = create_access_token(
        identity=user_found.id, expires_delta=timedelta(days=5))

    return access_token
