from flask_restx import Resource, Namespace
from implemented import user_service, auth_service
from flask import request

users_ns = Namespace('user')


@users_ns.route('/')
class UsersView(Resource):
    def get(self):
        token = request.headers["Authorization"].split("Bearer ")[-1]
        email = user_service.get_email_from_token(token)

        return user_service.get_user_by_email(email), 200

    def patch(self):
        data = request.json
        token = request.headers["Authorization"].split("Bearer ")[-1]
        email = user_service.get_email_from_token(token)
        user_service.change_user_info(data, email)

        return 'Changes saved', 200


@users_ns.route('/password/')
class UserView(Resource):
    def put(self):
        data = request.json
        token = request.headers["Authorization"].split("Bearer ")[-1]
        email = user_service.get_email_from_token(token)
        auth_service.change_password(data, email)
