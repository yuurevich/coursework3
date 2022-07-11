from flask import request
from flask_restx import Resource, Namespace
from implemented import director_service


directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    @directors_ns.response(200, 'Success')
    @directors_ns.response(404, 'Directors not found')
    def get(self):
        page = request.args.get('page')
        directors = director_service.get_all_directors(page)
        return directors, 200


@directors_ns.route('/<id>/')
class DirectorsView(Resource):
    @directors_ns.response(200, 'Success')
    @directors_ns.response(404, 'Directors not found')
    def get(self, id):
        return director_service.get_director(id), 200
