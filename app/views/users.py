""" User routes """


from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError

from app.models import db, User
from app.services.http import build_api_response
from app.serializer.users_schema import UserSchema


bp_users = Blueprint("api_users", __name__, url_prefix='/users')


@bp_users.route('', methods=['GET'])
@jwt_required
def list_users_or_add_user():

    if request.method == 'GET':
        users = User.query.all()
        return {'data': UserSchema(many=True).dump(users)}, HTTPStatus.OK

    # if request.method == 'POST':


@bp_users.route('/<int:id_user>', methods=['GET', 'DELETE', 'PATCH'])
@jwt_required
def get_delete_patch_specific_user(id_user):

    if request.method == 'GET':
        user = User.query.filter_by(id=id_user).first()

        if user is None:
            return build_api_response(HTTPStatus.NOT_FOUND)

        return {'data': UserSchema().dump(user)}

    if request.method == 'PATCH':

        db_user = User.query.filter_by(id=id_user).first()

        user = request.get_json(force=True)

        db_user.name = user.get('name') if user.get('name') else db_user.name
        db_user.email = user.get('email') if user.get(
            'email') else db_user.email
        db_user.password = user.get('password') if user.get(
            'password') else db_user.password
        db_user.is_admin = user.get('is_admin') if user.get(
            'is_admin') else db_user.is_admin

        db.session.commit()
        return {'data': UserSchema().dump(db_user)}

    if request.method == 'DELETE':

        user = User.query.filter_by(id=id_user).first()

        if user is None:
            return build_api_response(HTTPStatus.NOT_FOUND)

        db.session.delete(user)
        db.session.commit()

        return build_api_response(HTTPStatus.OK)
