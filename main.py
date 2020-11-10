from game_stuff import Game
from interactions import get_number_of_players
from interactions import get_first_player_name
from logging_stuff import Logger


def main():
    game_log = Logger("ticTacToeLogger")
    game_log.info("requesting username")
    player_one = get_first_player_name()
    number_of_players = get_number_of_players()
    game_board = Game(number_of_players, player_one)


if __name__ == '__main__':
    main()
