import random


class TicTacToeBoard:
    def __init__(self, board_grid: list, active_player: str, game_round: int):
        self.board_grid = board_grid
        self.active_player = active_player
        self.game_round = game_round

    @staticmethod
    def check_win_conditions(self) -> bool:
        print("There are " + str(self.board_grid.count('_')) + " empty spaces.")
        if self.board_grid[0][0] == self.board_grid[0][1] == self.board_grid[0][2] == self.active_player \
                or self.board_grid[1][0] == self.board_grid[1][1] == self.board_grid[1][2] == self.active_player \
                or self.board_grid[2][0] == self.board_grid[2][1] == self.board_grid[2][2] == self.active_player \
                or self.board_grid[0][0] == self.board_grid[1][0] == self.board_grid[2][0] == self.active_player \
                or self.board_grid[0][1] == self.board_grid[1][1] == self.board_grid[2][1] == self.active_player \
                or self.board_grid[0][2] == self.board_grid[1][2] == self.board_grid[2][2] == self.active_player \
                or self.board_grid[0][0] == self.board_grid[1][1] == self.board_grid[2][2] == self.active_player \
                or self.board_grid[2][2] == self.board_grid[1][1] == self.board_grid[0][0] == self.active_player:
            return True
        elif 1 == 5:
            # write a condition to detect CAT
            return True
        else:
            # Neither the win or the CAT conditions have been met, continue program
            return False

    @staticmethod
    def exit_program(self):
        print("The program will now exit!")
        # todo program exit code

    def increment_game_round(self):
        self.game_round += 1
        self.set_active_player()

    def place_mark(self, row: int, col: int):
        grid_position_to_be_marked = self.board_grid[row - 1][col - 1]
        if grid_position_to_be_marked == '_':  # if spot hasn't been marked
            print("Game : Grid selection successful, placing mark!")
            self.board_grid[row - 1][col - 1] = self.active_player
            self.print_grid()
        else:  # if spot has already been marked
            print("Game : This position is already full, please try again.")
            self.prompt_for_move()  # prompt the player to enter a new grid position

    @staticmethod
    def player_has_won(self) -> bool:
        win_conditions_met = game_board.check_win_conditions(self)
        if win_conditions_met:
            print("Game : The winner of the game is " + self.active_player)
            return True
        else:
            print("")
            return False

    def print_grid(self):
        print(str(self.board_grid[0]))
        print(str(self.board_grid[1]))
        print(str(self.board_grid[2]))

    def print_grid_location(self, row: int, column: int):
        if row < 1 or row > 3 or column < 1 or column > 3:
            print("Debug : Row or column selection is out of range")
        else:
            grid_value = self.board_grid[row - 1][column - 1]
            print("Debug : The grid_value is of the selected positions is " + str(grid_value))
            return grid_value

    def prompt_for_move(self):
        print("Game : Hello player " + str(self.active_player) + ", please make your move")
        print("Game : This is what the board looks like right now!")
        self.print_grid()
        row = input("Game : Please enter move row here >> ")
        col = input("Game : Please enter move column here >> ")
        row_is_numeric = row.isnumeric()
        col_is_numeric = col.isnumeric()
        row_and_col = self.verify_row_and_column_input(self, row, col, row_is_numeric, col_is_numeric)
        row = row_and_col[0]
        col = row_and_col[1]
        self.print_grid_location(row, col)
        print("Game : The selected row is " + str(row) +
              " and the selected column is " + str(col))
        self.place_mark(row, col)

    def set_active_player(self):  # called by self.increment_game_round()
        if self.game_round % 2 == 0:
            self.active_player = 'X'  # this player goes first (and when game_round is even)
            print("Game : The active player is " + str(self.active_player) + "!")
        else:
            self.active_player = 'O'  # this player goes when game_round is odd
            print("Game : The active player is " + str(self.active_player) + "!")

    @staticmethod
    def verify_row_and_column_input(self, row: int, col: int, row_is_numeric: bool, col_is_numeric: bool) -> list:
        print("Debug : Begin verify_row_and_column_input")
        row_and_col = [row, col]
        if not row_is_numeric or not col_is_numeric:
            print("Please use numeric input only.")
            row_and_col[0] = 2
            row_and_col[1] = 2
        else:
            row_and_col[0] = int(row)
            row_and_col[1] = int(col)
        if row_and_col[0] < 1 or row_and_col[0] > 3:
            row_and_col[0] = 2
        if row_and_col[1] < 1 or row_and_col[1] > 3:
            row_and_col[1] = 2
        return row_and_col
        print("Debug : End verify_row_and_column_input")


# initialize the TicTacToeBoard object as game_board with initial conditions
init_board_grid = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]  # empty starting grid
init_active_player = 'X'  # X will always go first
init_game_round = 1  # the game round starts at 1
game_board = TicTacToeBoard(init_board_grid, init_active_player, init_game_round)
while not game_board.player_has_won(game_board):
    game_board.increment_game_round()  # increment game_round
    game_board.prompt_for_move()  # allow the active_player to place a mark 'X' or 'O'
