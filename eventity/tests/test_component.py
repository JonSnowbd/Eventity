from eventity import ECSystem
from unittest import TestCase
import os

class TestComponent(TestCase):
    def test_correct_id(self):

        component = {
            "name": "test",
            "data": {
                "string": "Hello world!"
            }
        }

        mock_file_path = os.path.join(os.path.realpath(__file__), "..", "mock.entity")
        
        ecs = ECSystem()

        e1 = ecs.new().add(component)
        e2 = ecs.from_file(mock_file_path)

        self.assertTrue(e1.test["string"] == "Hello world!")

        self.assertTrue(e2.test["string"] == "Fly high!")
        self.assertTrue(e2.test["number"] is 100)

        self.assertTrue(e2.test2["strings"][0] == "String one!")
        self.assertTrue(e2.test2["strings"][1] == "String two!")
        self.assertTrue(e2.test2["strings"][2] == "String three!")

        self.assertTrue( isinstance(e2.test2["strings"], list) )

        del ecs
