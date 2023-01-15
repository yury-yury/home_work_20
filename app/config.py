class Config:
    """
    The class is used to configure application objects.
    Contains all the necessary variables to configure instances.
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
