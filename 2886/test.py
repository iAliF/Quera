import unittest

from q_2886 import get_time


class Test(unittest.TestCase):
    def test_one(self) -> None:
        self.assertEqual(get_time(3, 55), "09:05")

    def test_two(self) -> None:
        self.assertEqual(get_time(0, 0), "00:00")


if __name__ == '__main__':
    unittest.main()
