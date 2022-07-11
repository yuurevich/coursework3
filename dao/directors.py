from sqlalchemy import desc

from dao.model.directors import Directors, DirectorSchema


class DirectorsDAO:

    def __init__(self, session):
        self.session = session

    def get_all_directors(self, page):
        directors = Directors.query

        if page:
            page = int(page)
            directors = directors.paginate(page, 12, False)
            return DirectorSchema(many=True).dump(directors.items)

        return DirectorSchema(many=True).dump(directors)

    def get_director(self, did):
        director = Directors.query.filter(Directors.id == did).first()
        return DirectorSchema().dump(director)

