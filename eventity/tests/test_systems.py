from eventity import ECSystem, System, Component
from unittest import TestCase
import os

class TestSystem(System):
    def set_up(self, evt):
        evt.subscribe(self.do_it, "do_it")

    def do_it(self, data):
        for entity in self.ecs.list(["position"]):
            print entity
            entity.position["x"] += 10

class TestSystems(TestCase):
    def test_eventsystem(self):
        posComponent = Component("position", x=0, y=0)
        ecs = ECSystem()

        ecs.register(TestSystem)

        j = ecs.new("Jarl")
        ecs.add(j, posComponent)

        ecs.send("do_it")
        ecs.send("do_it")
        print ecs("Jarl").position
        self.assertTrue(ecs("Jarl").position["x"] == 20)
