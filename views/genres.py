from flask import request
from flask_restx import Resource, Namespace
from implemented import genre_service


genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    @genres_ns.response(200, 'Success')
    @genres_ns.response(404, 'Genres not found')
    def get(self):
        page = request.args.get('page')
        genres = genre_service.get_all_genres(page)
        return genres, 200


@genres_ns.route('/<id>/')
class GenreView(Resource):
    def get(self, id):
        return genre_service.get_genre(id), 200