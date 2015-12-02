"""Module implementing IO manipulation utilities."""

def get_player_name(number):
    """Returns a player name.

    :return: A name that the player chose for himself.
    :rtype: str
    """
    return input("Enter player {} name: ".format(number))


def get_player_symbol(input_function, number):
    """Returns a player symbol.

    This function bothers the player until a proper game symbol is entered.

    :return: A symbol that the player will use.
    :rtype: char (str of length 1)
    """
    symb = input_function("Enter player {} symbol: ".format(number))
    while len(symb) != 1:
        symb = input_function("Symbol must be a single character.\n"
                              "Enter player {} symbol: ".format(number))
    return symb


def get_int(msg):
    """Gets an integer from a player.

    This function keeps prompting the player with ``msg`` until he enters a
    valid integer.

    :param str msg: Message to prompt the user.
    :return: User inputted integer.
    :rtype: int
    """
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Please input an integer.")


def get_bool(msg, accepted=None, rejected=None):
    """Gets a bool from a player.

    This function keeps prompting the player with ``msg`` until
    an answer is recognized as positive or negative.
    Default values for ``accepted`` are ``{'y', 'yes', 'Y'}`` and for
    ``rejected`` are ``{'n', 'no', 'N'}``. If you wish to make one of the values
    default, specify an empty string as an accepted or rejected value.
    The ``rejected`` and ``accepted`` sequences should be disjoint, otherwise
    behaviour is implementation defined.

    :param str msg: Message to prompt the user.
    :param accepted: If user inputs any of items in this iterable, the
                     result is considered affirmative.
    :type accepted: iterable of str
    :param rejected: If the user inputs a string that appears in this iterable,
                     the answer is considered negative. If neither of the above
                     is the case, the user is promted again.
    :type rejected: iterable of str
    :return: User inputted boolean.
    :rtype: bool
    """
    if accepted is None:
        accepted = {'y', 'yes', 'Y'}
    if rejected is None:
        rejected = {'n', 'no', 'N'}

    while True:
        result = input(msg).strip()
        if result in accepted:
            return True
        if result in rejected:
            return False
