from flask import request
from flask_restx import Namespace, Resource

from container import auth_service

auth_ns = Namespace('auth')

@auth_ns.route('/')
class AuthView(Resource):
    """
    The AuthView class inherits from the Resource class of the flask_restx library and
    is a Base View class designed to process requests at the address "/auth/".
    """
    def post(self):
        """
        The function does not accept arguments and is designed to process a POST request at the address "/auth/",
        checks the user registration data in the database and implements the creation of short-term
        and long-term tokens necessary to access the endpoints of the application returns the created
        objects in the form of JSON.
        """
        data = request.json
        username = data.get("username", None)
        password = data.get("password", None)
        if None in [username, password]:
            return "", 400
        tokens = auth_service.generate_tokens(username, password)
        return tokens, 201

    def put(self):
        """
        The function does not accept arguments and is designed to process a PUT request at the address "/auth/",
        checks a long-term token and implements the creation of short-term and long-term tokens necessary
        to access the endpoints of the application returns the created objects in the form of JSON.
        """
        data = request.json
        token = data.get("refresh_token")
        tokens = auth_service.approve_refresh_token(token)
        return tokens, 201