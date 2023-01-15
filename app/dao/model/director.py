from marshmallow import Schema, fields

from app.database import db


class Director(db.Model):
    """
    The Director class inherits from the Model class of the flask_sqlalchemy library defines the model
    of the 'director' table of the database used.
    """
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    """
    The Directory Schema class inherits from the Schema class of the marshmallow library and defines the schema
    of the 'director' table of the database used for serialization and deserialization of objects.
    """
    id = fields.Int()
    name = fields.Str()
