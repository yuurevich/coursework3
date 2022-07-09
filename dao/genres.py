from dao.model.genres import Genres, GenreSchema


class GenresDAO:
    def __init__(self, session):
        self.session = session

    def get_all_genres(self):
        genres = Genres.query.all()
        return GenreSchema(many=True).dump(genres)

    def get_genre(self, gid):
        genre = Genres.query.filter(Genres.id == gid).first()
        return GenreSchema().dump(genre)
