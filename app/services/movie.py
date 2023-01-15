from app.dao.model.movie import Movie
from app.dao.movie import MovieDAO


class MovieService:
    """
    The MovieService service class is designed to link views and the database access object,
    and includes the necessary logic for working with received and transmitted data.
    """
    def __init__(self, dao: MovieDAO):
        """
        The function takes, as a parameter, an object of the MovieDAO class during initialization.
        """
        self.dao = dao

    def get_all_by_director_and_genre(self, did: int, gid: int):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_all_by_director_and_genre(did, gid)

    def get_all_by_director(self, did: int):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_all_by_director(did)

    def get_all_by_genre(self, gid: int):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_all_by_genre(gid)

    def get_all(self, page: int):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_all(page)

    def create(self, data: dict):
        """
        The function defines the method of the class .create takes data for creating a database object
        as a parameter, creates it and passes it for saving. Returns the created entity.
        """
        movie = Movie(**data)
        return self.dao.update(movie)

    def get_one(self, mid: int):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_one(mid)

    def update(self, data: dict):
        """
         The function defines the method of the class .update accepts data for updating a database object
         as a parameter updates it and passes it for saving. Returns the updated entity
        """
        mid = data.get("id")
        movie = self.get_one(mid)
        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")
        return self.dao.update(movie)

    def delete(self, mid: int):
        """
        The function defines the method of the class .delete takes the record ID
        as a parameter, requests a record with the corresponding parameter,
        and passes the resulting database object for deletion.
        """
        movie = self.get_one(mid)
        self.dao.delete(movie)



