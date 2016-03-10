def to_binary(n):
    s = []
    while n != 0:
        s.append(n % 2)
        n //= 2
    return ''.join(map(str, reversed(s)))
