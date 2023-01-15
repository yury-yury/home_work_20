from app.constants import LINES_PER_PAGE
from app.dao.model.movie import Movie


class MovieDAO:
    """
    The MovieDAO service class, which is Data Access Objects, is designed to perform
    all necessary operations with the database.
    """
    def __init__(self, session):
        """
        The function takes, as a parameter, a database access object during initialization.
        """
        self.session = session

    def get_all_by_director_and_genre(self, did, gid):
        """
        The function defines the method of the class .get_all_by_director_and_genre takes
        the ID of the director and the ID of the genre as parameters and queries all records
        of the "movie" table of the database containing these parameters in the corresponding
        columns and returns for further use. If there are no such records, returns an empty list.
        """
        return self.session.query(Movie).filter(Movie.director_id == did, Movie.genre_id == gid).all()

    def get_all_by_director(self, did: int):
        """
        The function defines the method of the class .get_all_by_director takes the director's ID
        as a parameter and queries all records of the "movie" table of the database containing
        this parameter in the corresponding column and returns for further use.
        If there are no such records, returns an empty list.
        """
        return self.session.query(Movie).filter(Movie.director_id == did).all()

    def get_all_by_genre(self, gid: int):
        """
        The function defines the method of the class .get_all_by_genre takes the genre ID as a parameter
        and queries all records of the "movie" table of the database containing this parameter
        in the corresponding column and returns for further use.
        If there are no such records, returns an empty list.
        """
        return self.session.query(Movie).filter(Movie.genre_id == gid).all()

    def get_all(self, page: int):
        """
        The function defines the method of the class .get_all takes the page number as a parameter
        and queries all records of the "genre" table of the database and performs
        its page-by-page return for further use.
        """
        return self.session.query(Movie).limit(LINES_PER_PAGE).offset((page - 1) * LINES_PER_PAGE).all()

    def get_one(self, mid: int):
        """
        The function defines the method of the class .get_one takes the row ID as a parameter
        and queries the "movie" table entry of the database containing this parameter
        in the corresponding column and returns for further use.
        """
        return self.session.query(Movie).get(mid)

    def update(self, movie: Movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, movie: Movie):
        """
        The function defines the method of the class .delete takes as a parameter
        an object of the "movie" table of the database and deletes it.
        """
        self.session.delete(movie)
        self.session.commit()
