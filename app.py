from flask_restx import Api
from flask import Flask, render_template
from config import Config
from migrate import migrate
from setup_db import db
from views.auth import auth_ns

from views.directors import directors_ns
from views.genres import genres_ns
from views.movies import movies_ns
from views.users import users_ns


api = Api(
    authorizations={
        "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    title="Flask Course Project 4",
    doc="/docs/",
)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()

    @app.route('/')
    def index():
        return render_template('index.html')

    api.init_app(app)
    db.init_app(app)
    db.create_all()
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(users_ns)
    # migrate()

    return app


if __name__ == '__main__':
    app = create_app(Config)
    app.run(port=25000, debug=True)