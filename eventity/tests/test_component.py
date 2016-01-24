from eventity import ECSystem, Component
from unittest import TestCase
import os

class TestComponent(TestCase):
    def test_correct_id(self):

        expected_dict = {
            "name": "test",
            "data": {
                "string": "Hello world!",
                "number": 10
            }
        }

        component = Component("test", string="Hello world!", number = 10)
        self.assertTrue(component.dict == expected_dict)

        ecs = ECSystem()

        e1 = ecs.new()
        ecs.add(e1, component, string="Not Hello world!")

        self.assertTrue(e1.test["string"] == "Not Hello world!")
        self.assertTrue(e1.test["number"] == 10)

        del ecs
