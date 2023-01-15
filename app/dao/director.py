from app.dao.model.director import Director


class DirectorDAO:
    """
    The DirectorDAO service class, which is Data Access Objects, is designed to perform
    all necessary operations with the database.
    """
    def __init__(self, session):
        """
        The function takes, as a parameter, a database access object during initialization.
        """
        self.session = session

    def get_all(self):
        """
        The function defines the method of the class .get_all and queries all records
        of the "director" table of the database and returns it for further use.
        """
        return self.session.query(Director).all()

    def get_one(self, did: int):
        """
        The function defines the method of the class .get_one takes the row ID as a parameter
        and queries the "director" table entry of the database containing this parameter
        in the corresponding column and returns for further use.
        """
        return self.session.query(Director).get(did)

    def update(self, director: Director):
        """
        The function defines the method of the class .update takes a database object as a parameter
        and writes and commits data to the "director" table of the database. Returns the accepted object.
        """
        self.session.add(director)
        self.session.commit()
        return director

    def delete(self, director: Director):
        """
        The function defines the method of the class .delete takes the "director" table object
        of the database as a parameter and deletes it.
        """
        self.session.delete(director)
        self.session.commit()
