from tictactoe import player, board, ioutil


class Game(object):
    def __init__(self, num_of_players, width, height):
        self.board = None
        self.width = width
        self.height = height
        self.num_of_players = num_of_players
        self.players = []
        self.round_counter = 0
        self.on_turn = 0

    def setup(self):
        for i in range(self.num_of_players):
            name = ioutil.get_player_name(i+1)
            symb = ioutil.get_player_symbol(input, i+1)
            self.players.append(player.Player(name, symb))

    def play_round(self):
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
                    print('Position {} invalid.')

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
        self.setup()
        while True:
            self.play_round()
            another = ioutil.get_bool("Want to play another round [Y/n]: ", accepted={'Y', 'y', '', 'yes'})
            if not another:
                self.goodbye()
                return

    def goodbye(self):
            print("Thank you for playing.")


if __name__ == '__main__':
    g = Game(2, 3, 3)
    g.mainloop()
