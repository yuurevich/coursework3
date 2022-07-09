from dao.model.movies import Movies, MovieSchema


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        movies = Movies.query.all()
        return MovieSchema(many=True).dump(movies)

    def get_movie(self, id):
        movie = Movies.query.filter(Movies.id == id).first()
        return MovieSchema().dump(movie)

