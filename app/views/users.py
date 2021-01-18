""" User routes """


from flask import Blueprint, request
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError

from app.models import db, User, UserSchema
from app.services.http import build_api_response
from app.serializer.users_schema import UserSchema


bp_users = Blueprint("api_users", __name__, url_prefix='/users')

@bp_users.route('', methods=['GET, POST'])
def list_users_or_add_user():
    
    if request.method == 'GET':
        users = User.query.all()
        return {'data': UserSchema(many=True).dump(users)}, HTTPStatus.OK

    if request.method == 'POST':
        data = request.get_json(force=True)
        user = User(
            name = data.get('name', None)
            email = data.get('email', None)
            password = data.get('password', None)
            is_admin = data.get('is_admin', None)
        )

        try:
            db.session.add(user)
            db.session.commit()

            return build_api_response(HTTPStatus.OK)

        except IntegrityError:
            return build_api_response(HTTPStatus.BAD_REQUEST)