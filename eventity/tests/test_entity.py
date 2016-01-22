from eventity import ECSystem
from unittest import TestCase

class TestEntity(TestCase):
    def test_correct_id(self):

        ecs = ECSystem()

        e1 = ecs.new("Charles")
        e2 = ecs.new()
        e3 = ecs.new()

        self.assertTrue(e1.id is "Charles")
        self.assertTrue(e2.id is 2)
        self.assertTrue(e3.id is 3)

        del ecs
