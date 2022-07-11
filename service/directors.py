from dao.directors import DirectorsDAO


class DirectorService:

    def __init__(self, directors_dao: DirectorsDAO):
        self.directors_dao = directors_dao

    def get_all_directors(self, page):
        return self.directors_dao.get_all_directors(page)

    def get_director(self, did):
        return self.directors_dao.get_director(did)

