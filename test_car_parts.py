import unittest
from car_parts import CarParts

class TestCarParts(unittest.TestCase):
    def setUp(self):
        self.car = CarParts()

    def test_get_parts(self):
        self.assertEqual(self.car.get_parts(), ['engine', 'wheels', 'brakes', 'seats', 'steering wheel'])

    def test_add_part(self):
        self.assertTrue(self.car.add_part('door'))
        self.assertIn('door', self.car.get_parts())
        self.assertFalse(self.car.add_part('engine'))

    def test_remove_part(self):
        self.assertTrue(self.car.remove_part('engine'))
        self.assertNotIn('engine', self.car.get_parts())
        self.assertFalse(self.car.remove_part('door'))

if __name__ == '__main__':
    unittest.main()
