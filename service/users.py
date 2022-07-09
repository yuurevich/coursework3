import jwt
from flask import current_app

from constants import JWT_SECRET, JWT_ALGORITHM
from dao.model.users import UserSchema
from dao.users import UsersDAO


class UserService:
    def __init__(self, users_dao: UsersDAO):
        self.users_dao = users_dao

    def get_user_by_email(self, email):
        return self.users_dao.get_user_by_email(email)

    def register(self, data):
        return self.users_dao.register(data)

    def get_email_from_token(self, token):

        decoded_token = jwt.decode(
            jwt=token,
            key=JWT_SECRET,
            algorithms=JWT_ALGORITHM
        )
        email = decoded_token.get('email')
        return email

    def change_user_info(self, data, email):
        return self.users_dao.change_user_info(data, email)


