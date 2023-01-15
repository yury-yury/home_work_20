from flask import request, jsonify
from flask_restx import Namespace, Resource

from app.dao.model.movie import MovieSchema
from app.decorators import auth_required, admin_required
from container import movie_service


movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    """
    The MovieView class inherits from the Resource class of the flask_restx library
    and is the base viewer class designed to handle all requests to the address "/movies/".
    """
    @auth_required
    def get(self):
        """
        The function defines a class method and is designed to process GET requests at "/movies/",
        tracks and organizes various types of movie searches: all movies, movies of a certain genre,
        movies of a certain director and movies of a certain director and genre.
        """
        if request.args.get("director_id") and request.args.get("genre_id"):
            did = int(request.args.get("director_id"))
            gid = int(request.args.get("genre_id"))
            movies = movie_service.get_all_by_director_and_genre(did, gid)
            return movies_schema.dump(movies)

        elif request.args.get("director_id"):
            did = int(request.args.get("director_id"))
            movies = movie_service.get_all_by_director(did)
            return movies_schema.dump(movies)

        elif request.args.get("genre_id"):
            gid = int(request.args.get("genre_id"))
            movies = movie_service.get_all_by_genre(gid)
            return movies_schema.dump(movies)

        else:
            page = request.args.get("page", 1, type=int)
            all_movies = movie_service.get_all(page)
            return movies_schema.dump(all_movies)

    @admin_required
    def post(self):
        """
        The function does not accept arguments and is designed to process a POST request to the address "/movies/",
        implements the creation of a new movie and writing it to the database,
        returns the created database object in the form of JSON.
        """
        req_json = request.json
        movie = movie_service.create(req_json)
        return movie_schema.dump(movie)


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    """
    he MovieView class inherits from the Resource class of the flask_rectx library and
    is a Base View class designed to process requests at the address "/movies/<int:mid>".
    """
    @auth_required
    def get(self, mid: int):
        """
        The function takes as an argument the id of the movie as an integer and is designed to process
        a GET request at the address "/movies/<int:mid>", implements a search for the movie in the database,
        returns the found database object in the form of JSON.
        """
        try:
            movie = movie_service.get_one(mid)
            return movie_schema.dump(movie)
        except Exception as e:
            return jsonify({"message": f"{e}"})

    @admin_required
    def put(self, mid: int):
        """
        The function takes as an argument the id of the movie as an integer and is designed to process
        a PUT request at the address "/movies/<int:mid>", implements the search and updating of movie data
        in the database, returns an updated database object in the form of JSON.
        """
        req_json = request.json
        req_json["id"] = mid
        movie = movie_service.update(req_json)
        return movie_schema.dump(movie)

    @admin_required
    def delete(self, mid: int):
        """
        The function takes as an argument the id of the movie as an integer and is designed to process
        a DELETE request at the address "/movies/<int:mid>", implements the search and deletion of the movie
        from the database, returns an empty string in the form of JSON.
        """
        movie_service.delete(mid)
        return ''
