from unittest.mock import MagicMock
import pytest

from app.dao.model.movie import Movie
from app.dao.movie import MovieDAO
from app.services.movie import MovieService


@pytest.fixture()
def movie_dao():
    """
    The utility function is designed to lock methods of the MovieDAO class
    and prepare test data to check the functioning of methods of the MovieService class.
    """
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title="Test_1", description="description_1", trailer="trailer_1",
                    year=2018, rating=8.6,	genre_id=1, director_id=1)
    movie_2 = Movie(id=2, title="Test_2", description="description_2", trailer="trailer_2",
                    year=2015, rating=7.8, genre_id=2, director_id=2)
    movie_3 = Movie(id=3, title="Test_3", description="description_3", trailer="trailer_3",
                    year=2010, rating=6.8, genre_id=3, director_id=3)

    movie_dao.get_all_by_director_and_genre = MagicMock(return_value=[movie_2])
    movie_dao.get_all_by_director = MagicMock(return_value=[movie_2])
    movie_dao.get_all_by_genre = MagicMock(return_value=[movie_2])
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.get_one = MagicMock(return_value=movie_2)
    movie_dao.update = MagicMock(return_value=movie_3)
    movie_dao.delete = MagicMock()

    return movie_dao


class TestMovieService():
    """
    The TestMovieService service class is designed to check the functioning of methods
    of the MovieService class and contains unit tests of all methods of the class being tested.
    """
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        """
        The service function - fixture of the TestMovieService class creates a test instance
        of the class to check the functioning of the methods of the MovieService class.
        """
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_all_by_director_and_genre(self):
        """
        The function contains unit tests to check the operability of the "get_all_by_director_and_genre" method
        of the MovieService class.
        """
        movies = self.movie_service.get_all_by_director_and_genre(2, 2)

        assert movies is not None
        assert type(movies) == list

    def test_get_all_by_director(self):
        """
        The function contains unit tests to check the operability of the "get_all_by_director" method
        of the MovieService class.
        """
        movies = self.movie_service.get_all_by_director(2)

        assert movies is not None
        assert type(movies) == list

    def test_get_all_by_genre(self):
        """
        The function contains unit tests to check the operability of the "get_all_by_genre" method
        of the MovieService class.
        """
        movies = self.movie_service.get_all_by_genre(2)

        assert movies is not None
        assert type(movies) == list

    def test_get_all(self):
        """
        The function contains unit tests to check the operability of the "get_all" method
        of the MovieService class.
        """
        movies = self.movie_service.get_all(1)

        assert len(movies) > 0
        assert movies[0] is not None
        assert type(movies) == list

    def test_create(self):
        """
        The function contains unit tests to check the operability of the "create" method
        of the MovieService class.
        """
        data = {"title": "Test_3", "description": "description_3", "trailer": "trailer_3",
                    "year": 2010, "rating": 6.8, "genre_id": 3, "director_id": 3}
        movie = self.movie_service.create(data)

        assert movie.id is not None
        assert movie.title == "Test_3"

    def test_get_one(self):
        """
        The function contains unit tests to check the operability of the "get_one" method
        of the MovieService class.
        """
        movie = self.movie_service.get_one(2)

        assert movie is not None
        assert movie.id == 2

    def test_update(self):
        """
        The function contains unit tests to check the operability of the "update" method
        of the MovieService class.
        """
        data = {"id": 3, "title": "Test_3", "description": "description_3", "trailer": "trailer_3",
                    "year": 2010, "rating": 6.8, "genre_id": 3, "director_id": 3}
        movie = self.movie_service.update(data)

        assert movie.id is not None
        assert movie.title == "Test_3"

    def test_delete(self):
        """
        The function contains unit tests to check the operability of the "delete" method
        of the MovieService class.
        """
        res = self.movie_service.delete(2)

        assert res is None
