from marshmallow import Schema, fields

from app.database import db


class Genre(db.Model):
    """
    The Genre class inherits from the Model class of the flask_sqlalchemy library defines the model
    of the 'genre' table of the database used.
    """
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    """
    The GenreSchema class inherits from the Schema class of the marshmallow library and defines the schema
    of the 'genre' table of the database used for serialization and deserialization of objects.
    """
    id = fields.Int()
    name = fields.Str()