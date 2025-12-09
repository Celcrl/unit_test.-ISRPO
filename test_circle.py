import unittest
import math
from circle import area, perimeter


class CircleShortTestCase(unittest.TestCase):
    # Тесты для функции area()
    def test_area_zero(self):
        result = area(0)
        self.assertEqual(result, 0)

    def test_area_normal(self):
        result = area(5)
        expected = math.pi * 25  # π * 5²
        self.assertAlmostEqual(result, expected)

    def test_perimeter_normal(self):
        result = perimeter(3)
        expected = 2 * math.pi * 3  # 6π
        self.assertAlmostEqual(result, expected)

    def test_perimeter_zero(self):
        result = perimeter(0)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()