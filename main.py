class TicTacToeBoard:
    def __init__(self, board_grid: list, active_player: str, game_round: int):
        self.board_grid = board_grid
        self.active_player = active_player
        self.game_round = game_round

    @staticmethod
    def check_win_conditions() -> bool:
        print("Win condition analysis here.")
        return True

    def increment_game_round(self):
        self.game_round += 1
        self.set_active_player()

    def place_mark(self, row: int, column: int):
        grid_position_to_be_marked = self.board_grid[row - 1][column - 1]  # player's chosen grid position
        if grid_position_to_be_marked == '_':  # if spot hasn't been marked
            print("Grid selection successful, placing mark!")
            grid_position_to_be_marked = self.active_player
        else:  # if spot has already been marked
            print("This position is already full, please try again.")
            grid_position_to_be_marked = self.active_player

    @staticmethod
    def player_has_won(self) -> bool:
        win_conditions_met = game_board.check_win_conditions()
        if win_conditions_met:
            print("The winner of the game is " + self.active_player)
        else:
            print("")

    def print_grid(self):
        print(str(self.board_grid[0]))
        print(str(self.board_grid[1]))
        print(str(self.board_grid[2]))

    def print_grid_location(self, row: int, column: int):
        grid_value = self.board_grid[row - 1][column - 1]
        print("The grid_value is " + str(grid_value))
        return grid_value

    def prompt_for_move(self):
        print("Hello player " + str(self.active_player) + ", please make your move")
        row = int(input("Please enter move row here >> "))
        column = int(input("Please enter move column here >> "))
        self.print_grid_location(row, column)
        print("The selected row is " + str(row) + " and the selected column is " + str(column))
        self.place_mark(row, column)

    def set_active_player(self):  # called by self.increment_game_round()
        if self.game_round % 2 == 0:
            self.active_player = 'X'  # this player goes first (and when game_round is even)
            print("The active player is " + str(self.active_player) + "!")
        else:
            self.active_player = 'O'  # this player goes when game_round is odd
            print("The active player is " + str(self.active_player) + "!")


# initialize the TicTacToeBoard object as game_board with initial conditions
init_board_grid = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]  # empty starting grid
init_active_player = 'X'  # X will always go first
init_game_round = 1  # the game round starts at 1
game_board = TicTacToeBoard(init_board_grid, init_active_player, init_game_round)

# start the game loop
while not game_board.player_has_won(game_board):
    game_board.set_active_player()  # select the active_player based on the game_round
    game_board.prompt_for_move()  # allow the active_player to place a mark 'X' or 'O'
    game_board.increment_game_round()  # increment game_round
