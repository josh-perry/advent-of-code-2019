import unittest

from day2 import day2


class TestIntcode(unittest.TestCase):
    def test_intcode_examples(self):
        param_list = [
            ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
            ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
            ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
            ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99])
        ]

        for i, expected in param_list:
            with self.subTest():
                day2.execute_intcode(i)
                self.assertEqual(i, expected)


if __name__ == '__main__':
    unittest.main()
