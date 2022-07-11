from dao.genres import GenresDAO


class GenreService:

    def __init__(self, genres_dao: GenresDAO):
        self.genres_dao = genres_dao

    def get_all_genres(self, page):
        return self.genres_dao.get_all_genres(page)

    def get_genre(self, gid):
        return self.genres_dao.get_genre(gid)
