from setup_db import db
from marshmallow import Schema, fields


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    favourite_genre = db.Column(db.String)


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favourite_genre = fields.Str()
