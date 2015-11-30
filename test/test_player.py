from tictactoe import player
import unittest


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = player.Player('Han', 'x')

    def test_init(self):
        self.assertEqual(self.player.name, 'Han')
        self.assertEqual(self.player.symbol, 'x')

if __name__ == '__main__':
    unittest.main()
