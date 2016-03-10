"""Module implementing player related funcionality."""


class Player(object):
    """Class holding basic player information."""

    def __init__(self, name, symbol):
        """Sets player name and symbol.

        :param str name: The name of the player.
        :param str symbol: The symbol that the player will use.

        >>> p = Player('John', 'x')
        >>> p.name
        'John'
        >>> p.symbol
        'x'
        """
        self.name = name
        self.symbol = symbol

    def __str__(self):
        """Returns player representation as a string.

        >>> print(Player('John', 'x'))
        John (x)
        """
        return "{} ({})".format(self.name, self.symbol)

    def __repr__(self):
        """Returns valid python code representing a player.

        >>> Player('John', 'x')
        Player('John', 'x')
        """
        return "Player('{}', '{}')".format(self.name, self.symbol)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
