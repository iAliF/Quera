import unittest

from q_10326 import func


class Test(unittest.TestCase):
    def test_one(self) -> None:
        self.assertEqual(func('3 2 1 3'), '1 1 0 0')

    def test_two(self) -> None:
        self.assertEqual(func('3 3 5 3'), '2 1 1 1')

    def test_three(self) -> None:
        self.assertEqual(func('4 2 5 3'), '2 2 2 1')


if __name__ == '__main__':
    unittest.main()
