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

    def add(self, component, **kwargs):
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
        if isinstance(component, Component):
            temp_dict = component.dict
        else:
            temp_dict = component
        temp = deepcopy(temp_dict)

        for key, value in kwargs.iteritems():
            temp["data"][key] = value

        setattr(self, temp["name"], temp["data"])
        return self

    def has(self, c_list = []):
        """
        Returns true if this entity has all the listed components within
        c_list.
        """
        for component in c_list:
            if not hasattr(self, component):
                return False

        return True
