import unittest

from day1 import day1


class TestSum(unittest.TestCase):
    def test_fuel_calculation(self):
        param_list = [
            (12, 2),
            (14, 2),
            (1969, 654),
            (100756, 33583)
        ]

        for i, expected in param_list:
            with self.subTest():
                fuel = day1.get_mass_fuel_requirement(i)
                self.assertEqual(fuel, expected)


if __name__ == '__main__':
    unittest.main()
