from data_validation import argument_is_alpha
from data_validation import argument_is_digit
from human_stuff import Player


def ask_number_of_players():
    try:
        number_of_players = input("how many people are playing? [1] or [2]\n")
        if argument_is_digit(number_of_players) and 0 < int(number_of_players) < 3:
            return number_of_players
        else:
            print("sorry that is not a valid response, try again")
            return ask_number_of_players()
    except IOError as player_input_error:
        raise player_input_error


def greet_user_and_set_name():
    try:
        name_ = input("hey player, what is your name_?\n")
        if argument_is_alpha(name_):
            person = Player(name_)
            print("cool, hi " + person.user_name + "\n")
            return person
    except IOError as username_error:
        raise username_error
