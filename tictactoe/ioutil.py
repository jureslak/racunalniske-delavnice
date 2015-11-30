def get_player_name(number):
    return input("Enter player {} name: ".format(number))


def get_player_symbol(input_function, number):
    symb = input_function("Enter player {} symbol: ".format(number))
    while len(symb) != 1:
        symb = input_function("Symbol must be a single character.\n"
                              "Enter player {} symbol: ".format(number))
    return symb


def get_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Please input an integer.")


def get_bool(msg, accepted=None, rejected=None):
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
