"""Module implementing basic game functionality."""


class Board(object):
    """Class representing a playing board."""

    def __init__(self, width, height, players):
        """Initializes an empty board."""
        self.width = width
        self.height = height
        self.grid = [[None for i in range(width)] for j in range(height)]
        self.players = players
        self.win_length = 3
        self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]

    def __str__(self):
        """Nicely prints the current board.

        >>> from tictactoe.player import Player
        >>> b = Board(3, 3, [Player('Leia', 'x')])
        >>> b.grid[1][1] = 0  # player number 0
        >>> print(b)
        +---+---+---+
        | 1 | 2 | 3 |
        +---+---+---+
        | 4 | x | 6 |
        +---+---+---+
        | 7 | 8 | 9 |
        +---+---+---+
        """

        r = []
        field_width = len(str(self.width * self.height)) + 2
        for i, v in enumerate(self.grid):
            line = []
            for j, c in enumerate(v):
                if c is None:
                    line.append("{0: ^{1}d}".format(i * self.width + j + 1, field_width))
                else:
                    line.append("{0: ^{1}s}".format(self.players[c].symbol, field_width))
            r.append('|' + '|'.join(line) + '|\n')

        separator = '+' + '+'.join('-'*field_width for i in range(self.width)) + '+\n'
        text = separator + separator.join(r) + separator
        return text.strip()

    def set(self, position, player_index):
        """Sets a player symbol to position.

        >>> b = Board(3, 3, [])
        >>> b.set(1, 0)
        >>> b.grid[0][0]
        0
        >>> b.set(1, 0)
        Traceback (most recent call last):
        ...
        ValueError: Position '1' is taken.
        """

        if not 1 <= position <= self.width * self.height:
            raise ValueError("Position '{}' is out of range.".format(position))
        y = (position - 1) // self.height
        x = (position - 1) % self.width
        if self.grid[y][x] is not None:
            raise ValueError("Position '{}' is taken.".format(position))

        self.grid[y][x] = player_index

    def finished(self):
        """Checks if the game has finished and reports the outcome.

        Returns a tuple of two elements.
        First one is a bool telling us if the game has finished.
        The second one is the winner, if it exists, or None otherwise.

        >>> b = Board(3, 3, [])
        >>> b.set(1, 0)
        >>> b.set(5, 0)
        >>> b.finished()
        (False, None)
        >>> b.set(9, 0)
        >>> b.finished()
        (True, 0)
        """

        done = True
        for i in range(self.height):
            for j in range(self.width):
                candidate = self.grid[i][j]
                if candidate is None:
                    done = False
                    continue
                for dx, dy in self.directions:
                    if (0 <= i + dy*(self.win_length-1) < self.height and
                            0 <= j + dx*(self.win_length-1) < self.width):
                        for k in range(1, self.win_length):
                            if self.grid[i + dy*k][j + dx*k] != candidate:
                                break
                        else:
                            return (True, candidate)
        return (done, None)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
