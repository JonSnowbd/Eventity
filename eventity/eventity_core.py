from .entity import Entity
from .eventmanager import EventManager
from .entityfileparser import parse_entity

pool = []
systems = []
evt = EventManager()

class ECSystem(object):
    """
    The beef of the Framework. This is instanciated in the init file to allow
    easy ecs(search id) formats
    """

    def __call__(self, search):
        return self.get_id(search)

    def new(self, Entity_ID = None):
        """
        Define a new entity, with an option to define the ID manually rather
        than let the system give it a number.
        """
        if Entity_ID is None:
            tempID = len(pool)+1
        else:
            if self.exists(Entity_ID): return None
            tempID = Entity_ID

        tempent = Entity(tempID)
        pool.append(tempent)

        return pool[-1]

    def from_file(self, file_path, Entity_ID=None):
        temp = self.new(Entity_ID)
        for component in parse_entity(file_path):
            temp.add(component)

    def list(self, Search_ID = None):
        """
        Return a filtered list of the entities with certain components. If components
        are not given to the method, simply return all entities.
        """
        ret_array = []
        if Search_ID is None:
            return pool
        else:
            for entity in pool:
                if entity.has(Search_ID) is True:
                    ret_array.append(entity)
            return ret_array

    def get_id(self, Search_ID):
        """
        Get an entity with a certain ID. Used by the __call__ attr of the ECS.
        """
        for entity in self.list():
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
        temp = system_class(evt, self.list, self)
        systems.append(temp)

    def send(self, trigger, data = {}):
        """
        Broadcasts an event to all systems.
        """
        evt.trigger(trigger, data)
