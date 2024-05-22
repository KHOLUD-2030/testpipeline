import unittest
from car_parts import CarParts

class TestCarParts(unittest.TestCase):

    def test_list_parts(self):
        parts = CarParts.list_parts()
        self.assertIsInstance(parts, list)
        self.assertGreater(len(parts), 0)
        self.assertIn('Engine', parts)

    def test_part_available(self):
        self.assertTrue(CarParts.part_available('Engine'))
        self.assertFalse(CarParts.part_available('Spoiler'))

if __name__ == '__main__':
    unittest.main()
