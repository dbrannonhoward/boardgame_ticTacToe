from interactions import ask_number_of_players
from interactions import greet_user_and_set_name
from logging_stuff import Logger


def main():
    game_log = Logger("ticTacToeLogger")
    game_log.info("greeting user, requesting username")
    person_with_name = greet_user_and_set_name()
    number_of_players = ask_number_of_players()


if __name__ == '__main__':
    main()
