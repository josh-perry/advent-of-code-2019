import unittest

from day3 import day3


class TestCrossedWires(unittest.TestCase):
    def test_crossed_wires_examples(self):
        param_list = [
            (['R75','D30','R83','U83','L12','D49','R71','U7','L72','U62','R66','U55','R34','D71','R55','D58','R83'], 159)
        ]

        for i, expected in param_list:
            with self.subTest():
                self.assertEqual(i, expected)


if __name__ == '__main__':
    unittest.main()
