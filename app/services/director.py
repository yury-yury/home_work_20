from app.dao.director import DirectorDAO
from app.dao.model.director import Director


class DirectorService:
    """
    The DirectorService service class is designed to link views and the database access object,
    and includes the necessary logic for working with received and transmitted data.
    """
    def __init__(self, dao: DirectorDAO):
        """
        The function takes, as a parameter, an object of the DirectorDAO class during initialization.
        """
        self.dao = dao

    def get_all(self):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_all()

    def create(self, data: dict):
        """
        The function defines the method of the class .create takes data for creating a database object
        as a parameter, creates it and passes it for saving. Returns the created entity.
        """
        director = Director(**data)
        return self.dao.update(director)

    def get_one(self, did: int):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_one(did)

    def update(self, data: dict):
        """
        The function defines the method of the class .update accepts data for updating a database object
        as a parameter updates it and passes it for saving. Returns the updated entity
        """
        did = data.get("id")
        director = self.get_one(did)
        director.name = data.get("name")
        return self.dao.update(director)

    def delete(self, did: int):
        """
        The function defines the method of the class .delete takes the record ID
        as a parameter, requests a record with the corresponding parameter,
        and passes the resulting database object for deletion.
        """
        director = self.get_one(did)
        self.dao.delete(director)



