"""A module for handling binary numbers as strings."""


def to_binary(n):
    """Converts a given integer to binary.

    >>> to_binary(0)
    '0'
    >>> to_binary(-2)
    '-10'
    >>> to_binary(5)
    '101'
    >>> to_binary(1023)
    '1111111111'
    >>> to_binary(3.14)
    Traceback (most recent call last):
    ...
    ValueError: Only integer values are supported.
    """

    if not isinstance(n, int):
        raise ValueError('Only integer values are supported.')

    n = int(n)  # for bool
    if n == 0:
        return '0'
    if n < 0:
        return '-' + to_binary(-n)

    s = []
    while n > 0:
        s.append(n % 2)
        n //= 2
    return ''.join(map(str, reversed(s)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
