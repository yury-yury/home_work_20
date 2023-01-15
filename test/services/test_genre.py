from unittest.mock import MagicMock
import pytest

from app.dao.model.genre import Genre
from app.dao.model.movie import Movie
from app.dao.genre import GenreDAO
from app.services.genre import GenreService


@pytest.fixture()
def genre_dao():
    """
    The utility function is designed to lock methods of the GenreDAO class
    and prepare test data to check the functioning of methods of the GenreService class.
    """
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name="Комедия")
    genre_2 = Genre(id=2, name="Семейный")
    genre_3 = Genre(id=3, name="Фэнтези")
    movie_1 = Movie(id=1, title="Test_1", description="description_1", trailer="trailer_1",
                    year=2018, rating=8.6,	genre_id=2, director_id=1)
    movie_2 = Movie(id=2, title="Test_2", description="description_2", trailer="trailer_2",
                    year=2015, rating=7.8, genre_id=2, director_id=2)

    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3])
    genre_dao.get_one = MagicMock(return_value=genre_2)
    genre_dao.get_list_movie_by_genre = MagicMock(reurn_value=[movie_1, movie_2])
    genre_dao.update = MagicMock(return_value=genre_3)
    genre_dao.delete = MagicMock()

    return genre_dao


class TestGenreService():
    """
    The TestGenreService service class is designed to check the functioning of methods
    of the GenreService class and contains unit tests of all methods of the class being tested.
    """
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        """
        The service function - fixture of the TestGenreService class creates a test instance
        of the class to check the functioning of the methods of the GenreService class.
        """
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_all(self):
        """
        The function contains unit tests to check the operability of the "get_all" method
        of the GenreService class.
        """
        genres = self.genre_service.get_all()

        assert type(genres) == list
        assert len(genres) > 0
        assert genres[0] is not None

    def test_create(self):
        """
        The function contains unit tests to check the operability of the "create" method
        of the GenreService class.
        """
        data = {"name": "Фэнтези"}
        genre = self.genre_service.create(data)

        assert genre.id is not None
        assert genre.name == "Фэнтези"

    def test_get_one_with_movie(self):
        """
        The function contains unit tests to check the operability of the "get_one_with_movie" method
        of the GenreService class.
        """
        genre_dict = self.genre_service.get_one_with_movie(2)

        assert genre_dict is not None
        assert genre_dict["movies"] is not None

    def test_update(self):
        """
        The function contains unit tests to check the operability of the "update" method
        of the GenreService class.
        """
        data = {"id": 3, "name": "Фэнтези"}
        genre = self.genre_service.update(data)

        assert genre.id is not None
        assert genre.name == "Фэнтези"

    def test_delete(self):
        """
        The function contains unit tests to check the operability of the "delete" method
        of the GenreService class.
        """
        res = self.genre_service.delete(2)

        assert res is None
