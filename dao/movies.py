from flask import current_app

from dao.model.movies import Movies, MovieSchema
from sqlalchemy import desc


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self, page, status):
        movies = Movies.query
        if status == 'new':
            movies = movies.order_by(desc(Movies.year))

        if page:
            page = int(page)
            movies = movies.paginate(page, 12, False)
            return MovieSchema(many=True).dump(movies.items)
        
        return MovieSchema(many=True).dump(movies)

    def get_movie(self, id):
        movie = Movies.query.filter(Movies.id == id).first()
        return MovieSchema().dump(movie)

