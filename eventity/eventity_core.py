from .entity import Entity
from pubsub import pub
from copy import deepcopy
from sets import Set

class ECSystem(object):
    """
    The beef of the Framework. This is instanciated in the init file to allow
    easy ecs(search id) formats
    """
    def __init__(self):
        self.pool = {
            "default": []
        }
        self.pool_cache = {}
        self.systems = []
        self.evt = pub

    def __call__(self, search):
        return self.get_id(search)

    def new(self, Entity_ID = None):
        """
        Define a new entity, with an option to define the ID manually rather
        than let the system give it a number.
        """
        if Entity_ID is None:
            tempID = len(self.pool["default"])+1
        else:
            if self.exists(Entity_ID): return None
            tempID = Entity_ID

        tempent = Entity(tempID)
        self.pool["default"].append(tempent)

        return self.pool["default"][-1]

    def add(self, entity, component, **kwargs):
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
        temp_dict = component.dict
        temp = deepcopy(temp_dict)

        for key, value in kwargs.iteritems():
            temp["data"][key] = value


        setattr(entity, temp["name"], temp["data"])
        try:
            self.pool[temp["name"]].add(entity)
        except KeyError:
            self.pool[temp["name"]] = set([])
            self.pool[temp["name"]].add(entity)
        return self

    def list(self, search_array = None):
        """
        Return a filtered list of the entities with certain components. If components
        are not given to the method, simply no entities.
        """
        if search_array is None:
            return
            yield

        try:
            entity_list = set.intersection(*[self.pool[x] for x in search_array])
        except KeyError:
            return
            yield

        for ent in entity_list:
            yield ent

    def get_id(self, Search_ID):
        """
        Get an entity with a certain ID. Used by the __call__ attr of the ECS.
        """
        for entity in self.pool["default"]:
            if entity.id == Search_ID:
                return entity

        return None

    def exists(self, Search_ID):
        """
        Check if an entity exists with a certain ID in the current pool. True if it
        does, False if it doesnt.
        """
        if self.get_id(Search_ID) is None:
            return False
        else:
            return True

    def register(self, system_class):
        """
        Register a system into the... Well system. Binds all the events
        into the eventmanager
        """
        temp = system_class(self.evt, self.list, self)
        self.systems.append(temp)

    def send(self, trigger, **kwargs):
        """
        Broadcasts an event to all systems.
        """
        temp_data = {}
        for key, value in kwargs.iteritems():
            temp_data[key] = value
        self.evt.sendMessage(trigger, data=temp_data)
