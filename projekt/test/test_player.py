from tictactoe import player
import unittest


class PlayerTest(unittest.TestCase):
    """Test player functionality."""

    def setUp(self):
        """Set up a sample player used throughout this test."""
        self.player = player.Player('Han', 'x')

    def test_init(self):
        """Test initialization."""
        self.assertEqual(self.player.name, 'Han')
        self.assertEqual(self.player.symbol, 'x')

    def test_str(self):
        """Test string representation."""
        self.assertEqual(str(self.player), 'Han (x)')

    def test_repr(self):
        """Test repr string representation."""
        self.assertEqual(repr(self.player), "Player('Han', 'x')")

if __name__ == '__main__':
    unittest.main()
