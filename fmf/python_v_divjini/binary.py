"""Module for handling binary numbers."""


def to_binary(n: int) -> str:
    """
    Converts given integer to its binary representation.
    :param n: The integer to convert.
    :return: A string with binary representation of `n`.

    >>> [to_binary(i) for i in range(-3, 3)]
    ['-11', '-10', '-1', '0', '1', '10']
    >>> to_binary(-6)
    '-110'
    >>> to_binary("40")
    Traceback (most recent call last):
    ...
    TypeError: Only integral values are accepted, got 'str'.
    """
    if not isinstance(n, int):
        raise TypeError("Only integral values are accepted, got '{}'.".format(n.__class__.__name__))
    
    if n == 0:
        return '0'  
    if n < 0:
        return '-' + to_binary(-n)

    # Euclid's algorithm
    stevke = []
    while n > 0:
        stevke.append(n % 2)
        n //= 2
    return ''.join(map(str, reversed(stevke)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
