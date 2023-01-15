from marshmallow import Schema, fields

from app.database import db


class User(db.Model):
    """
    The User class inherits from the Model class of the flask_sqlalchemy library defines the model
    of the 'user' table of the database used.
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    role = db.Column(db.String(255))


class UserSchema(Schema):
    """
    The UserSchema class inherits from the Schema class of the marshmallow library and defines the schema
    of the 'user' table of the database used for serialization and deserialization of objects.
    """
    id = fields.Int(dump_only=True)
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()
