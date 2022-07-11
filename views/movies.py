from flask import request
from flask_restx import Resource, Namespace
from implemented import movie_service


movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    @movies_ns.response(200, 'Success')
    @movies_ns.response(404, 'Movies not found')
    def get(self):
        page = request.args.get('page')
        status = request.args.get('status')
        movies = movie_service.get_movies(page, status)
        return movies, 200


@movies_ns.route('/<id>/')
class MovieView(Resource):
    @movies_ns.response(200, 'Success')
    @movies_ns.response(404, 'Movie not found')
    def get(self, id):
        movie = movie_service.get_movie(id)
        return movie, 200
