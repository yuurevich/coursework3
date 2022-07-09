from dao.model.directors import Directors, DirectorSchema


class DirectorsDAO:

    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        directors = Directors.query.all()
        return DirectorSchema(many=True).dump(directors)

    def get_director(self, did):
        director = Directors.query.filter(Directors.id == did).first()
        return DirectorSchema().dump(director)

