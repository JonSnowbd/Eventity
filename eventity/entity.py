from copy import deepcopy
from .component import Component

class Entity(object):
    """
    Entity has an id and methods to manipulate the current components,
    and nothing more.

    Preferably strings and numbers are to be used for IDs.
    """
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "<Entity " + str(self.id) + ">"

    def has(self, c_list = []):
        """
        Returns true if this entity has all the listed components within
        c_list.
        """
        for component in c_list:
            if not hasattr(self, component):
                return False

        return True
