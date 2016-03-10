"""Module implementig game logic."""

from tictactoe import player, board, ioutil


class Game(object):
    """Implementation of a complete game of Tic Tac Toe."""

    def __init__(self, num_of_players, width, height):
        """Construct a game.

        :param int num_of_players: Number of players.
        :param int width: Width of the field.
        :param int height: Height of the field.

        >>> g = Game(5, 3, 3)
        >>> g.num_of_players
        5
        >>> g.width
        3
        >>> g.height
        3
        """
        self.board = None
        self.width = width
        self.height = height
        self.num_of_players = num_of_players
        self.players = []
        self.round_counter = 0
        self.on_turn = 0

    def setup(self):
        """Performs game setup.

        This function repeatedly asks for ``num_of_players`` player names and
        their symbols. In further development, more setup tasks may be performed
        here.
        """
        for i in range(self.num_of_players):
            name = ioutil.get_player_name(i+1)
            symb = ioutil.get_player_symbol(input, i+1)
            self.players.append(player.Player(name, symb))

    def play_round(self):
        """Plays one round of a game.

        A round start with an empty board and players make their moves in turn,
        until one is victorious or the board is filled.
        """
        self.board = board.Board(self.width, self.height, self.players)
        self.round_counter += 1
        while True:
            print('Currently on turn: {}.'.format(self.players[self.on_turn]))
            print(self.board)

            while True:
                position = ioutil.get_int('Please input a position: ')
                try:
                    self.board.set(position, self.on_turn)
                    break
                except ValueError:
                    print('Position {} invalid.'.format(position))

            outcome, winner = self.board.finished()
            if outcome:
                print(self.board)
                if winner is None:
                    print("It's a tie!")
                else:
                    print("Player {} won!".format(self.players[winner]))
                break

            self.on_turn += 1
            self.on_turn %= self.num_of_players

    def mainloop(self):
        """Runs the whole game.

        First :func:`setup` is called. Then :func:`play_round` is called
        indefinitely, until player does not want another round. After that,
        :func:`goodbye` is called.
        """
        self.setup()
        while True:
            self.play_round()
            another = ioutil.get_bool("Want to play another round [Y/n]: ", accepted={'Y', 'y', '', 'yes'})
            if not another:
                self.goodbye()
                return

    def goodbye(self):
        """Post game cleanup.

        Now it only prints a goodbye message, but work could be done here if
        needed lateer on.
        """
        print("Thank you for playing.")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
