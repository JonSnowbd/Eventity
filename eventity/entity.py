from copy import deepcopy

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

    def add(self, component, custom_data = None):
        """
        Adds a component to the entity, accessible through the dot operator
        eg. ecs("player").position["x"]

        the component is taken in the form of a dict, as follows:
        {
            "name": "position",
            "data": {
                "x": 0,
                "y": 0
            }
        }
        """
        temp = deepcopy(component)# Required to make transaction non-referential
        if custom_data is None:
            setattr(self, temp["name"], temp["data"])
        else:
            setattr(self, temp["name"], custom_data)

        return self

    def has(self, c_list = []):
        """
        Returns true if this entity has all the listed components within
        c_list.
        """
        for component in c_list:
            try:
                getattr(self, component)
            except AttributeError:
                return False

        return True
