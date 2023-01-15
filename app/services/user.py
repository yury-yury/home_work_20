import base64
import hashlib
import hmac

from app.constants import PWD_SALT, PWD_ITERATIONS
from app.dao.user import UserDAO
from app.dao.model.user import User


class UserService:
    """
    The UserService service class is designed to link views and the database access object,
    and includes the necessary logic for working with received and transmitted data.
    """
    def __init__(self, dao: UserDAO):
        """
        The function takes, as a parameter, an object of the UserDAO class during initialization.
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
        data["password"] = self.generate_password(data.get("password"))
        user = User(**data)
        return self.dao.update(user)

    def get_one(self, uid: int):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_one(uid)

    def get_by_username(self, username):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_by_username(username)

    def update(self, data: dict):
        """
        The function defines the method of the class .update accepts data for updating a database object
        as a parameter updates it and passes it for saving. Returns the updated entity
        """
        uid = data.get("id")
        user = self.get_one(uid)
        user.name = data.get("name")
        return self.dao.update(user)

    def delete(self, uid: int):
        """
        The function defines the method of the class .delete takes the record ID
        as a parameter, requests a record with the corresponding parameter,
        and passes the resulting database object for deletion.
        """
        user = self.get_one(uid)
        self.dao.delete(user)

    def generate_password(self, password):
        """
        The function takes the user's password as an argument in the form of a string and is designed
        to hash the password in order to protect the stored information. Returns the password hash.
        """
        hash_digest = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), PWD_SALT, PWD_ITERATIONS)
        return base64.b64encode(hash_digest)

    def compare_password(self, password_hash, other_password):
        """
        The function takes as arguments the hash of the user's password stored in the database
        and the entered password in the form of a string and is designed to verify the entered data.
        Returns True if the correct data is entered, otherwise False.
        """
        decoded_digest = base64.b64decode(password_hash)
        hash_digest = hashlib.pbkdf2_hmac('sha256', other_password.encode('utf-8'), PWD_SALT, PWD_ITERATIONS)
        return hmac.compare_digest(decoded_digest, hash_digest)
