def argument_is_alpha(input_: str):
    try:
        if input_.isalpha():
            return True
        return False
    except IOError as alpha_error:
        raise alpha_error


def argument_is_digit(input_: str):
    try:
        if input_.isdigit():
            return True
        return False
    except IOError as digit_error:
        raise digit_error


def player_quantity_is_valid(input_):
    try:
        if 0 < input_ < 3:
            return True
        return False
    except ArithmeticError as player_error:
        raise player_error
