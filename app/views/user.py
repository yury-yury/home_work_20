from flask import request
from flask_restx import Namespace, Resource

from app.dao.model.user import UserSchema
from container import user_service

user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_ns.route('/')
class UsersView(Resource):
    """
    The UsersView class inherits from the Resource class of the flask_restx library and
    is a Base View class designed to process requests at the address "/users/".
    """
    def get(self):
        """
        The function does not accept arguments and is designed to process GET requests at the address "/users/",
        implements a search for all users in the database, returns the found data in the form of JSON.
        """
        users = user_service.get_all()
        return users_schema.dump(users)

    def post(self):
        """
        The function does not accept arguments and is designed to process a POST request to the address "/users/",
        implements the creation of a new user and writing it to the database,
        returns the created database object in the form of JSON.
        """
        req_json = request.json
        new_user = user_service.create(req_json)
        return user_schema.dump(new_user)


@user_ns.route('/<int:uid>')
class UserView(Resource):
    """
    The UserView class inherits from the Resource class of the flask_restx library and
    is a Base View class designed to process requests at the address "/users/<int:uid>".
    """
    def get(self, uid: int):
        """
        The function takes as an argument the ID of the user in the form of an integer and is intended
        for processing a GET request to the address "/users/<in:uid>", implements a search for
        a user in the database,returns the found database object in the form of JSON.
        """
        user = user_service.get_one(uid)
        return user_schema.dump(user)

    def put(self, uid: int):
        """
        The function takes as an argument the ID of the user in the form of an integer and is intended
        for processing the PUT request to the address "/users/<int:uid>", implements the search and updating
        of data about the user returns an updated database object in the form of JSON in the database.
        """
        req_json = request.json
        req_json["id"] = uid
        user = user_service.update(req_json)
        return user_schema.dump(user)


    def delete(self, uid: int):
        """
        The function takes as an argument the id of the user as an integer and is designed to process
        a DELETE request at the address "/users/<int:uid>", implements the search and deletion
        of the user from the database, returns an empty string in the form of JSON.
        """
        user_service.delete(uid)
        return ''
