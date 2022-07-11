from dao.movies import MoviesDAO


class MovieService:
    def __init__(self, movies_dao: MoviesDAO):
        self.movies_dao = movies_dao

    def get_movies(self, page, status):
        return self.movies_dao.get_all_movies(page, status)

    def get_movie(self, id):
        return self.movies_dao.get_movie(id)
