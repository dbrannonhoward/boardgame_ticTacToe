from CONSTANTS import VERSUS_CPU
from CONSTANTS import VERSUS_PLAYER
from graphics import SWEET_GAME_BOARD


class Game:
    def __init__(self, number_of_players, player_one, player_two=None):
        self.number_of_players = number_of_players
        self.game_board = SWEET_GAME_BOARD
        self.game_type = VERSUS_CPU
        self.player_one = player_one
        self.player_two = None
        if self.number_of_players == VERSUS_PLAYER:
            self.game_type = VERSUS_PLAYER
            self.player_two = player_two


    def assign_teams(self):
        pass


    def start_new_game(self):
        self.game_board = SWEET_GAME_BOARD
        self.check_if_two_player_game()
        self.assign_teams(self.game_type)
