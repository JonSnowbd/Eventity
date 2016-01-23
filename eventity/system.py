class System(object):
    def __init__(self, eventmanager, entities, ecs):
        self.ecs = ecs
        self.set_up(eventmanager)
