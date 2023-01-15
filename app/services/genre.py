from app.dao.genre import GenreDAO
from app.dao.model.genre import Genre


class GenreService:
    """
    The GenreService service class is designed to link views and the database access object,
    and includes the necessary logic for working with received and transmitted data.
    """
    def __init__(self, dao: GenreDAO):
        """
        The function takes, as a parameter, an object of the GenreDAO class during initialization.
        """
        self.dao = dao

    def get_all(self):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_all()

    def create(self, data: dict):
        """
        The function defines the method of the class .create takes data for creating a database object
        as a parameter, creates it and passes it for saving. Returns the created entity.
        """
        genre = Genre(**data)
        return self.dao.update(genre)

    def get_one_with_movie(self, gid: int):
        """
        The function defines the method of the class .get_one_with_movie takes the genre ID as a parameter,
        makes requests from the database object data acquisition object with the corresponding parameter
        and a list of related objects from the "movie" table, generates response data in the form
        of a dictionary and returns them.
        """
        genre = self.dao.get_one(gid)
        movies = self.dao.get_list_movie_by_genre(gid)
        movies_list = list()
        for item in movies:
            movies_list.append(item.title)
        return {"id": genre.id, "name": genre.name, "movies": movies_list}

    def update(self, data: dict):
        """
        The function defines the method of the class .update accepts data for updating a database object
        as a parameter updates it and passes it for saving. Returns the updated entity
        """
        gid = data.get("id")
        genre = self.dao.get_one(gid)
        genre.name = data.get("name")
        return self.dao.update(genre)

    def delete(self, gid: int):
        """
        The function defines the method of the class .delete takes the record ID
        as a parameter, requests a record with the corresponding parameter,
        and passes the resulting database object for deletion.
        """
        genre = self.dao.get_one(gid)
        self.dao.delete(genre)
