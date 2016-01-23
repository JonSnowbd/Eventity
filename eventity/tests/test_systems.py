from eventity import ECSystem, System
from unittest import TestCase
import os

class TestSystem(System):
    def set_up(self, evt):
        evt.subscribe(self.do_it, "do_it")

    def do_it(self, data):
        for entity in self.ecs.list(["position"]):
            entity.position["x"] += 10

class TestSystems(TestCase):
    def test_eventsystem(self):
        posComponent = {
            "name": "position",
            "data": {
                "x": 0,
                "y": 0
            }
        }
        ecs = ECSystem()

        ecs.register(TestSystem)

        ecs.new("Jarl").add(posComponent)

        ecs.send("do_it")
        ecs.send("do_it")

        self.assertTrue(ecs("Jarl").position["x"] == 20)
