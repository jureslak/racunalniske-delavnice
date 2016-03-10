from tictactoe import game, player
import unittest
from unittest import mock

class GameTest(unittest.TestCase):

    def setUp(self):
        self.num_of_players = 2
        self.width = 3
        self.height = 3
        self.game = game.Game(2, 3, 3)

    def test_init(self):
        self.assertEqual(self.game.board, None)
        self.assertEqual(self.game.width, self.width)
        self.assertEqual(self.game.height, self.height)
        self.assertEqual(self.game.num_of_players, self.num_of_players)
        self.assertEqual(self.game.players, [])
        self.assertEqual(self.game.round_counter, 0)
        self.assertEqual(self.game.on_turn, 0)

    def test_setup(self):
        input_seq = ['Luke', 'x', 'Leia', 'o']
        with mock.patch('builtins.input', side_effect=input_seq):
            self.game.setup()
        expected = [('Luke', 'x'), ('Leia', 'o')]
        for e, p in zip(expected, self.game.players):
            self.assertEqual(p.name, e[0])
            self.assertEqual(p.symbol, e[1])

    def test_play_round(self):
        # setup
        input_seq = ['Luke', 'x', 'Leia', 'o']
        with mock.patch('builtins.input', side_effect=input_seq):
            self.game.setup()

        input_seq = ['2', '5', '3', '1', '9', '6', '7', '4']
        with mock.patch('builtins.input', side_effect=input_seq):
            self.game.play_round()

        finished, winner = self.game.board.finished()
        self.assertTrue(finished)
        self.assertEqual(winner, 1)
        expected_board = [[1, 0, 0], [1, 1, 1], [0, None, 0]]
        self.assertEqual(self.game.board.grid, expected_board)
