from flask import request
from flask_restx import Namespace, Resource

from app.dao.model.director import DirectorSchema
from app.decorators import auth_required, admin_required
from container import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@director_ns.route('/')
class DirectorsView(Resource):
    """
    The Directory view class inherits from the Resource class of the flask_restx library and
    is a Base View class designed to process requests at the address "/directors/".
    """
    @auth_required
    def get(self):
        """
        The function does not accept arguments and is designed to process GET requests at the address "/directors/",
        implements a search for all directors in the database, returns the found data in the form of JSON.
        """
        directors = director_service.get_all()
        return directors_schema.dump(directors)

    @admin_required
    def post(self):
        """
        The function does not accept arguments and is designed to process a POST request to the address "/directors/",
        implements the creation of a new director and writing it to the database,
        returns the created database object in the form of JSON.
        """
        req_json = request.json
        new_director = director_service.create(req_json)
        return director_schema.dump(new_director)


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    """
    The Directory View class inherits from the Resource class of the flask_restx library and
    is a Base View class designed to process requests at the address "/directors/<int:did>".
    """
    @auth_required
    def get(self, did: int):
        """
        The function takes as an argument the ID of the director in the form of an integer and is intended
        for processing a GET request to the address "/directors/<in:did>", implements a search for
        a director in the database,returns the found database object in the form of JSON.
        """
        director = director_service.get_one(did)
        return director_schema.dump(director)

    @admin_required
    def put(self, did: int):
        """
        The function takes as an argument the ID of the director in the form of an integer and is intended
        for processing the PUT request to the address "/directors/<int:did>", implements the search and updating
        of data about the director returns an updated database object in the form of JSON in the database.
        """
        req_json = request.json
        req_json["id"] = did
        director = director_service.update(req_json)
        return director_schema.dump(director)

    @admin_required
    def delete(self, did: int):
        """
        The function takes as an argument the id of the director as an integer and is designed to process
        a DELETE request at the address "/directors/<int:did>", implements the search and deletion
        of the director from the database, returns an empty string in the form of JSON.
        """
        director_service.delete(did)
        return ''
