import unittest

from q_91712 import func


class Test(unittest.TestCase):
    def test_right(self) -> None:
        self.assertEqual(func(0, 2), "RR")

    def test_eq(self) -> None:
        self.assertEqual(func(1, 1), "Saal Noo Mobarak!")

    def test_three(self) -> None:
        self.assertEqual(func(1, 0), "L")


if __name__ == '__main__':
    unittest.main()
