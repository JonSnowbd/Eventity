class System(object):
    def __init__(self, eventmanager, entities, ecs):
        self.ecs = ecs
        self.limits = []
        self.entities = lambda:entities(self.limits)
        self.set_up(eventmanager)
