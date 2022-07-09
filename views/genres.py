from flask_restx import Resource, Namespace
from implemented import genre_service


genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all_genres()
        return genres, 200


@genres_ns.route('/<id>/')
class GenreView(Resource):
    def get(self, id):
        return genre_service.get_genre(id), 200