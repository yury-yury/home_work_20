from app.dao.model.genre import Genre
from app.dao.model.movie import Movie


class GenreDAO:
    """
    The GenreDAO service class, which is Data Access Objects, is designed to perform
    all necessary operations with the database.
    """
    def __init__(self, session):
        """
        The function takes, as a parameter, a database access object during initialization.
        """
        self.session = session

    def get_all(self):
        """
        The function defines the method of the class .get_all and queries all records
        of the "genre" table of the database and returns it for further use.
        """
        return self.session.query(Genre).all()

    def get_one(self, gid: int):
        """
        The function defines the method of the class .get_one takes the row ID as a parameter
        and queries the "movie" table entry of the database containing this parameter
        in the corresponding column and returns for further use.
        """
        return self.session.query(Genre).get(gid)

    def get_list_movie_by_genre(self, gid: int):
        """
         The function defines the method of the class .get_list_by_genre takes the genre ID as a parameter
        and queries all records of the "movie" table of the database containing this parameter
        in the corresponding column and returns for further use.
        If there are no such records, returns an empty list.
        """
        return self.session.query(Movie).filter(Movie.genre_id == gid).all()

    def update(self, genre: Genre):
        """
        The function defines the method of the class .update takes a database object as a parameter
        and writes and commits data to the "genre" table of the database. Returns the accepted object.
        """
        self.session.add(genre)
        self.session.commit()
        return genre

    def delete(self, genre: Genre):
        """
        The function defines the method of the class .delete takes as a parameter
        an object of the "genre" table of the database and deletes it.
        """
        self.session.delete(genre)
        self.session.commit()
