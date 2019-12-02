import unittest

from day1 import day1


class TestSum(unittest.TestCase):
    def test_fuel_calculation(self):
        param_list = [
            (14, 2),
            (1969, 966),
            (100756, 50346)
        ]

        for i, expected in param_list:
            with self.subTest():
                fuel = day1.get_total_fuel_for_mass(i)
                self.assertEqual(fuel, expected)


if __name__ == '__main__':
    unittest.main()
