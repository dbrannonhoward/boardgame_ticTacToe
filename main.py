import random


class TicTacToeBoard:
    def __init__(self, board_grid: list, active_player: str, game_round: int):
        self.board_grid = board_grid
        self.active_player = active_player
        self.game_round = game_round

    @staticmethod
    def check_win_conditions(self) -> bool:
        if self.board_grid[0][0] == self.board_grid[0][1] == self.board_grid[0][2] == self.active_player \
                or self.board_grid[1][0] == self.board_grid[1][1] == self.board_grid[1][2] == self.active_player \
                or self.board_grid[2][0] == self.board_grid[2][1] == self.board_grid[2][2] == self.active_player \
                or self.board_grid[0][0] == self.board_grid[1][0] == self.board_grid[2][0] == self.active_player \
                or self.board_grid[0][1] == self.board_grid[1][1] == self.board_grid[2][1] == self.active_player \
                or self.board_grid[0][2] == self.board_grid[1][2] == self.board_grid[2][2] == self.active_player \
                or self.board_grid[0][0] == self.board_grid[1][1] == self.board_grid[2][2] == self.active_player \
                or self.board_grid[2][2] == self.board_grid[1][1] == self.board_grid[0][0] == self.active_player:
            return True
        else:
            return False

    def increment_game_round(self):
        self.game_round += 1
        self.set_active_player()

    def place_mark(self, row: int, column: int):
        grid_position_to_be_marked = self.board_grid[row - 1][column - 1]
        if grid_position_to_be_marked == '_':  # if spot hasn't been marked
            print("Grid selection successful, placing mark!")
            self.board_grid[row - 1][column - 1] = self.active_player
            self.print_grid()
        else:  # if spot has already been marked
            print("This position is already full, please try again.")
            self.prompt_for_move()  # prompt the player to enter a new grid position

    @staticmethod
    def player_has_won(self) -> bool:
        win_conditions_met = game_board.check_win_conditions(game_board)
        if win_conditions_met:
            print("The winner of the game is " + self.active_player)
            return True
        else:
            print("")
            return False

    def print_grid(self):
        print(str(self.board_grid[0]))
        print(str(self.board_grid[1]))
        print(str(self.board_grid[2]))

    def print_grid_location(self, row: int, column: int):
        print("Row is type " + str(type(row)) + " and column is type " + str(type(column)))
        grid_value = self.board_grid[row - 1][column - 1]
        print("The grid_value is of the selected positions is " + str(grid_value))
        return grid_value

    def prompt_for_move(self):
        print("Hello player " + str(self.active_player) + ", please make your move")
        print("This is what the board looks like right now!")
        self.print_grid()
        row = int(input("Please enter move row here >> "))
        # row = self.verify_row_column_input(row)
        column = int(input("Please enter move column here >> "))
        # column = self.verify_row_column_input(column)
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

    @staticmethod
    def verify_row_column_input(row_or_col):
        coerced_row_col = row_or_col
        if row_or_col < 1 or row_or_col > 3:
            coerced_row_col = 4 * int(random.random())
            print("Your input value was invalid, fine.. I'll do it for you.")
            return int(coerced_row_col)


# initialize the TicTacToeBoard object as game_board with initial conditions
print("Initial conditions")
init_board_grid = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]  # empty starting grid
init_active_player = 'X'  # X will always go first
init_game_round = 1  # the game round starts at 1
game_board = TicTacToeBoard(init_board_grid, init_active_player, init_game_round)
while not game_board.player_has_won(game_board):
    game_board.increment_game_round()  # increment game_round
    game_board.prompt_for_move()  # allow the active_player to place a mark 'X' or 'O'
