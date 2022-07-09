import json

from dao.model.directors import Directors
from dao.model.genres import Genres
from dao.model.movies import Movies
from setup_db import db

with open('fixtures.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


def migrate():

    movies = []
    for movie in data['movies']:
        movie['id'] = movie.pop('pk')
        movies.append(Movies(**movie))
    with db.session.begin():
        db.session.add_all(movies)

    genres = []
    for genre in data['genres']:
        genre['id'] = genre.pop('pk')
        genres.append(Genres(**genre))
    with db.session.begin():
        db.session.add_all(genres)

    directors = []
    for director in data['directors']:
        director['id'] = director.pop('pk')
        directors.append(Directors(**director))
    with db.session.begin():
        db.session.add_all(directors)

