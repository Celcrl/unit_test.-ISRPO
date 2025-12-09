import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_normal(self):
        res = area(5, 4)
        self.assertEqual(res, 20)

    def test_perimeter_zero(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_normal(self):
        res = perimeter(5, 10)
        self.assertEqual(res, 30)

if __name__ == "__main__":
    unittest.main()