from flask import request, jsonify
from flask_restx import Namespace, Resource

from app.dao.model.genre import GenreSchema
from app.decorators import auth_required, admin_required
from container import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    """
    The GenresView class inherits from the Resource class of the flask_restx library and
    is a Base View class designed to process requests at the address "/genres/".
    """
    @auth_required
    def get(self):
        """
        The function does not accept arguments and is designed to process GET requests at the address "/genres/",
        implements a search for all genres in the database, returns the found data in the form of JSON.
        """
        genres = genre_service.get_all()
        return genres_schema.dump(genres)

    @admin_required
    def post(self):
        """
        The function does not accept arguments and is designed to process a POST request at the address "/genres/",
        implements the creation of a new genre and writing it to the database,
        returns the created database object in the form of JSON.
        """
        req_json = request.json
        new_genre = genre_service.create(req_json)
        return genre_schema.dump(new_genre)


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    """
    The GenreView class inherits from the Resource class of the flask_restx library and
    is a Base View class designed to process requests at "/genres/<int:gid>".
    """
    @auth_required
    def get(self, gid: int):
        """
        The function takes as an argument the genre identifier in the form of an integer and is intended
        for processing a GET request at the address "/genres/<in:gid>", implements a genre search
        in the database, returns the found database object in the form of JSON.
        """
        res = genre_service.get_one_with_movie(gid)
        return jsonify(res)

    @admin_required
    def put(self, gid: int):
        """
        The function takes as an argument the genre identifier in the form of an integer and is intended
        for processing request PUT at "/genres/<int:gid>", implements the search and updating of genre data
        in the database, returns the updated database object in the form of JSON.
        """

        req_json = request.json
        req_json["id"] = gid
        genre = genre_service.update(req_json)
        return genre_schema.dump(genre)

    @admin_required
    def delete(self, gid):
        """
        The function takes as an argument the genre id as an integer and is designed to process
        a DELETE request at the address "/genres/<int:gid>", implements the search and deletion
        of the genre from the database, returns an empty string in the form of JSON.
        """
        genre_service.delete(gid)
        return ''
