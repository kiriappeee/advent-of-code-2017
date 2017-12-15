import unittest
from . import day1solution as solution

class TestDay1Solution(unittest.TestCase):
    def test_1122_returns_3(self):
        self.assertEqual(solution.solve_captcha("1122"), 3, "captcha for 1122 should return 3")
    def test_1111_returns_4(self):
        self.assertEqual(solution.solve_captcha("1111"), 4)
    def test_1234_returns_0(self):
        self.assertEqual(solution.solve_captcha("1234"), 0)
    def test_91212129_returns_9(self):
        self.assertEqual(solution.solve_captcha("91212129"), 9)


if __name__ == "__main__":
    unittest.main()