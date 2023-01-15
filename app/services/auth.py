import calendar
import datetime

import jwt
from flask_restx import abort

from app.constants import JWT_SECRET, JWT_ALGORITHM
from app.services.user import UserService


class AuthService:
    """
    The Auth Service class is designed to ensure the functioning of user authentication
    and includes the necessary logic for working with received and transmitted data.
    """
    def __init__(self, user_service: UserService):
        """
        The function takes, as a parameter, an object of the UserService class during initialization.
        """
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refresh=False):
        """
        The function accepts the following data as positional parameters: the user name, the user password
        in the form of strings and the named parameter "is_refresh" in the form of True or False, defining
        a request to update a short-term token. The function generates short-term and long-term tokens.
        Returns the created objects as a dictionary.
        """
        user = self.user_service.get_by_username(username)
        if user is None:
            raise abort(404)
        if not is_refresh:
            if not self.user_service.compare_password(user.password, password):
                abort(400)
        data = {"username": user.username, "role": user.role}

        # 30 minutes for access_token
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        # 130 days for refresh_token
        day130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(day130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return {"access_token": access_token, "reresh_token": refresh_token}

    def approve_refresh_token(self, refresh_token):
        """
        The function takes a long-term user token as a parameter, decodes it and generates
        a request to update short-term and long-term tokens.
        """
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        username = data.get("username")
        return self.generate_tokens(username, None, is_refresh=True)
