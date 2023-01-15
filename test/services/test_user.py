from unittest.mock import MagicMock
import pytest

from app.dao.model.user import User
from app.dao.user import UserDAO
from app.services.user import UserService


@pytest.fixture()
def user_dao():
    """
    The utility function is designed to lock methods of the UserDAO class
    and prepare test data to check the functioning of methods of the UserService class.
    """
    user_dao = UserDAO(None)

    user_1 = User(id=2, username="oleg", password="nePl4BfTTMW+TIHNef+bkLp5V8uGfsmtL7Zz1P5Ff5U=", role="user")
    user_2 = User(id=3, username="john", password="Cl63UZctBNY5nscyTHO9gQnAdN0mEyJ7toia6qSp454=", role="admin")
    user_3 = User(id=4, username="alice", password="rnS9BDglDZXPg1ZqfiAFL5bJOrmymOi7H5adjbNrnGU=", role="user")

    user_dao.get_all = MagicMock(return_value=[user_1, user_2, user_3])
    user_dao.get_one = MagicMock(return_value=user_2)
    user_dao.get_by_username = MagicMock(return_value=user_3)
    user_dao.update = MagicMock(return_value=user_1)
    user_dao.delete = MagicMock()

    return user_dao


class TestUserService():
    """
    The TestUserService service class is designed to check the functioning of methods
    of the UserService class and contains unit tests of all methods of the class being tested.
    """
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao):
        """
        The service function - fixture of the TestUserService class creates a test instance
        of the class to check the functioning of the methods of the UserService class.
        """
        self.user_service = UserService(dao=user_dao)

    def test_get_all(self):
        """
        The function contains unit tests to check the operability of the "get_all" method
        of the UserService class.
        """
        users = self.user_service.get_all()

        assert len(users) > 0
        assert users[0] is not None

    def test_create(self):
        """
        The function contains unit tests to check the operability of the "create" method
        of the UserService class.
        """
        data = {"username": "oleg", "password": "12345", "role": "user"}
        user = self.user_service.create(data)

        assert user is not None
        assert user.id is not None
        assert user.username == "oleg"

    def test_get_one(self):
        """
        The function contains unit tests to check the operability of the "get_one" method
        of the UserService class.
        """
        user = self.user_service.get_one(3)

        assert user is not None
        assert user.id is not None

    def test_get_by_username(self):
        """
        The function contains unit tests to check the operability of the "get_by_username" method
        of the UserService class.
        """
        user = self.user_service.get_by_username("alice")

        assert user is not None
        assert user.id is not None
        assert user.username == "alice"

    def test_update(self):
        """
        The function contains unit tests to check the operability of the "update" method
        of the UserService class.
        """
        data = {"id": 2, "username": "oleg", "password": "12345", "role": "user"}
        user = self.user_service.update(data)

        assert user.id is not None
        assert user.username == "oleg"

    def test_delete(self):
        """
        The function contains unit tests to check the operability of the "delete" method
        of the UserService class.
        """
        res = self.user_service.delete(2)

        assert res is None

    def test_generate_password(self):
        """
        The function contains unit tests to check the operability of the "generate_password" method
        of the UserService class.
        """
        password_hash = self.user_service.generate_password("12345")

        assert password_hash is not None
        assert password_hash == b"S0gaYvvHJTMF/4+tTKN4kplnAMudGqHpDif8Ed/5FN0="

    def test_compare_password(self):
        """
        The function contains unit tests to check the operability of the "compare_password" method
        of the UserService class.
        """
        res = self.user_service.compare_password("S0gaYvvHJTMF/4+tTKN4kplnAMudGqHpDif8Ed/5FN0=", "12345")

        assert res is not None
        assert res == True
