from tictactoe import board, player
import unittest

class BoardTest(unittest.TestCase):
    """Test Board functionality."""

    def setUp(self):
        self.width = 3
        self.height = 3
        self.players = [player.Player('Luke', 'x'), player.Player('Leia', 'o')]
        self.board = board.Board(self.width, self.height, self.players)
        self.directions = [(-1, -1), (-1,  0), (-1, 1), (0, 1),
                            (0, -1),  (1, -1),  (1, 0), (1, 1)]

    def test_init(self):
        self.assertEqual(self.board.height, self.height)
        self.assertEqual(self.board.width, self.width)
        self.assertEqual(self.board.players, self.players)
        self.assertEqual(self.board.win_length, 3)
        self.assertEqual(self.board.directions, self.directions)
        self.assertEqual(self.board.grid, [[None] * self.width] * self.height)

    def test_set(self):
        self.board.set(1, 1)
        self.assertEqual(self.board.grid[0][0], 1)  # this one is set
        for i in range(self.width):                 # and the others are not
            for j in range(self.height):
                if i == 0 and j == 0: continue
                self.assertEqual(self.board.grid[j][i], None)
        self.assertRaisesRegex(ValueError, "Position '1' is taken.",
                               self.board.set, 1, 1)
        self.assertRaisesRegex(ValueError, "Position '-1' is out of range.",
                               self.board.set, -1, 9)
        self.board.set(2, 1)
        self.assertEqual(self.board.grid[0][1], 1)
        self.board.set(7, 8)
        self.assertEqual(self.board.grid[2][0], 8)
        self.board.set(5, 0)
        self.assertEqual(self.board.grid[1][1], 0)
        self.board.set(9, 5)
        self.assertEqual(self.board.grid[2][2], 5)
        self.board.set(6, 1)
        self.assertEqual(self.board.grid[1][2], 1)

    def test_win_ld(self):
        """Test left diagonal win case."""
        pass

    def test_win_rd(self):
        """Test right diagonal win case."""
        pass

    def test_win_lr(self):
        """Test left right win case."""
        pass

    def test_win_ud(self):
        """Test up down win case."""
        pass

    def test_no_win_on_none(self):
        """Test that 3 None's in a row are not a win."""
        pass

    def test_win_on_full(self):
        """Test that you can win in last move."""
        pass

    def test_no_win_on_full(self):
        """Test that a tie is an option."""
        pass

