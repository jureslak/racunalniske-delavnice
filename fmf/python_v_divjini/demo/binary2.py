"""A module for handling binary numbers as strings."""


def to_binary(n):
    """Converts a given integer to binary."""
    s = []
    while n != 0:
        s.append(n % 2)
        n //= 2
    return ''.join(map(str, reversed(s)))
