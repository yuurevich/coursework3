from dao.directors import DirectorsDAO


class DirectorService:

    def __init__(self, directors_dao: DirectorsDAO):
        self.directors_dao = directors_dao

    def get_all_directors(self):
        return self.directors_dao.get_all_directors()

    def get_director(self, did):
        return self.directors_dao.get_director(did)

