from flask import Flask
from flask_restx import Api

from app.config import Config
from app.database import db
from app.views.auth import auth_ns
from app.views.director import director_ns
from app.views.genre import genre_ns
from app.views.movie import movie_ns
from app.views.user import user_ns


def create_app(config: Config):
    """
    The function takes as an argument an instance of the configuration class, creates
    and configures an instance of the Flask class. Returns the created instance .
    """
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()
    return app


def configur_app(app: Flask):
    """
    The function takes as an argument an instance of the Flask class. Initializes
    an instance of the SQLAlchemy class, creates an instance of the Api class,
    and registers created instances of the Namespace class from the flask_restx module.
    """
    db.init_app(app)
    api = Api(app)

    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


if __name__ == '__main__':

    app_config = Config()
    app = create_app(app_config)
    configur_app(app)
    app.run()
