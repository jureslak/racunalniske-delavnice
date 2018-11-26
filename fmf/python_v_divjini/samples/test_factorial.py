from math import factorial
import unittest


class TestFactorial(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_positive(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(13.0), 6227020800)

    def test_invalid(self):
        self.assertRaises(ValueError, factorial, -1)
        self.assertRaises(ValueError, factorial, 1.6)
        self.assertRaises(TypeError, factorial, '23')
        self.assertRaises(TypeError, factorial, [12])
        self.assertRaises(OverflowError, factorial, 1348123481273489123493423)


if __name__ == '__main__':
    unittest.main()
