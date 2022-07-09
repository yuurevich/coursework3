from exceptions import UserNotFound, WrongPasswords, UserAlreadyExists
from service.users import UserService
from flask import abort, request
import calendar
import jwt
import base64
import hashlib
import hmac
from datetime import datetime, timedelta
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, JWT_SECRET, JWT_ALGORITHM


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def login(self, email, password):
        user = self.user_service.get_user_by_email(email)
        if user is None:
            raise UserNotFound

        password_hash = self.__generate_password(password)
        if not self.compare_password(user['password'], password_hash):
            raise WrongPasswords

        return self.__generate_tokens(user)

    def register(self, data):
        if self.user_service.get_user_by_email(data['email']) is not None:
            raise UserAlreadyExists

        data['password'] = self.__generate_password(data['password'])
        return self.user_service.register(data)

    def __generate_password(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
            )
        return base64.b64encode(hash_digest)

    def compare_password(self, password1, password2):
        password1 = base64.b64decode(password1)
        password2 = base64.b64decode(password2)
        return hmac.compare_digest(password1, password2)

    def __generate_tokens(self, user):
        if user is None:
            abort(404, 'User not found')

        data = {
            'email': user['email']
        }

        min30 = datetime.utcnow() + timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        days130 = datetime.utcnow() + timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return {
            'refresh_token': refresh_token,
            'access_token': access_token
        }

    def change_password(self, data, email):
        user = self.user_service.get_user_by_email(email)
        new_password = data.get('new_password')
        user_password = user['password']
        old_password = self.__generate_password(data.get('old_password'))

        if not self.compare_password(user_password, old_password):
            raise WrongPasswords
        new_password = self.__generate_password(new_password)
        data = {"password": new_password }

        self.user_service.change_user_info(data, email)
        print('пароль изменен')