from marshmallow import Schema, fields

from app.database import db


class Movie(db.Model):
    """
    The Movie class inherits from the Model class of the flask_sqlalchemy library defines the model
    of the 'movie' table of the database used.
    """
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class MovieSchema(Schema):
    """
    The MovieSchema class inherits from the Schema class of the marshmallow library and defines the schema
    of the 'movie' table of the database used for serialization and deserialization of objects.
    """
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    year = fields.Int()
    trailer = fields.Str()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
