from dao.model.users import Users, UserSchema


class UsersDAO:
    def __init__(self, session):
        self.session = session

    def register(self, data):
        user = Users(**data)
        self.session.add(user)
        self.session.commit()

    def get_user_by_email(self, email):
        user = Users.query.filter(Users.email == email).first()
        if user is not None:
            return UserSchema().dump(user)
        return None

    def get_user_by_id(self, id):
        user = Users.query.filter(Users.id == id).first()
        if user is not None:
            return UserSchema().dump(user)
        return None

    def change_user_info(self, data, email):
        Users.query.filter(Users.email == email).update(UserSchema().dump(data))
        self.session.commit()