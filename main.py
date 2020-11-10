from game_stuff import Game
from interactions import ask_number_of_players
from interactions import greet_user_and_set_name
from logging_stuff import Logger


def main():
    game_log = Logger("ticTacToeLogger")
    game_log.info("requesting username")
    player_one = greet_user_and_set_name()
    number_of_players = ask_number_of_players()
    game_board = Game(number_of_players, player_one)


if __name__ == '__main__':
    main()
