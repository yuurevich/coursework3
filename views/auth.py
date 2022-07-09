from flask import request, abort
from flask_restx import Resource, Namespace
from implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthRegister(Resource):
    def post(self):
        data = request.json
        print(data)
        email = data.get("email", None)
        password = data.get("password", None)

        if None in [email, password]:
            abort(400, 'Email or password not found')
        auth_service.register(data)
        # tokens = auth_service.generate_tokens(email, password)

        return 'Registration completed successfully', 200


@auth_ns.route('/login/')
class AuthLogin(Resource):
    def post(self):
        data = request.json

        email = data.get("email", None)
        password = data.get("password", None)

        if None in [email, password]:
            abort(400, 'Incorrect email or password')

        tokens = auth_service.login(email, password)

        return tokens, 201

    def put(self):
        data = request.json
        refresh_token = data.get("refresh_token")

        if refresh_token is None:
            abort(400, 'refresh_token not found')

        tokens = auth_service.approve_refresh_token(refresh_token)

        return tokens, 201