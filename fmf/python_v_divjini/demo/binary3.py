"""A module for handling binary numbers as strings."""


def to_binary(n):
    """Converts a given integer to binary.

    >>> to_binary(1)
    '1'
    >>> to_binary(2)
    '10'
    >>> to_binary(5)
    '101'
    >>> to_binary(1023)
    '1111111111'
    """

    s = []
    while n != 0:
        s.append(n % 2)
        n //= 2
    return ''.join(map(str, reversed(s)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
