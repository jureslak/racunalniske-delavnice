import binary5
import unittest

class BinaryTestCase(unittest.TestCase):
    """Tests for binary5 module."""

    def test_zero(self):
        self.assertEqual("0", binary5.to_binary(0))
        self.assertEqual("0", binary5.to_binary(-0))
        self.assertEqual("0", binary5.to_binary(False))

    def test_positive(self):
        self.assertEqual("1", binary5.to_binary(1))
        self.assertEqual("1", binary5.to_binary(True))
        self.assertEqual("10", binary5.to_binary(2))
        self.assertEqual("11", binary5.to_binary(3))
        self.assertEqual("101", binary5.to_binary(5))
        self.assertEqual("11010", binary5.to_binary(26))
        self.assertEqual("1000000", binary5.to_binary(64))
        self.assertEqual("1111111", binary5.to_binary(127))

    def test_negative(self):
        self.assertEqual("-1", binary5.to_binary(-1))
        self.assertEqual("-10", binary5.to_binary(-2))
        self.assertEqual("-11", binary5.to_binary(-3))
        self.assertEqual("-101", binary5.to_binary(-5))
        self.assertEqual("-11010", binary5.to_binary(-26))
        self.assertEqual("-1000000", binary5.to_binary(-64))
        self.assertEqual("-1111111", binary5.to_binary(-127))

    def test_error(self):
        self.assertRaisesRegex(ValueError, "Only integer values are supported.",
                               binary5.to_binary, 2.0)
        self.assertRaisesRegex(ValueError, "Only integer values are supported.",
                               binary5.to_binary, (1,))
        self.assertRaisesRegex(ValueError, "Only integer values are supported.",
                               binary5.to_binary, "12")
        self.assertRaisesRegex(ValueError, "Only integer values are supported.",
                               binary5.to_binary, 3+5j)
        self.assertRaisesRegex(ValueError, "Only integer values are supported.",
                               binary5.to_binary, [-4])

if __name__ == '__main__':
    unittest.main()
