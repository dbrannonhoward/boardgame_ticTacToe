from random import random


def coerce_values(row, col):
    row_and_col = [row, col]
    print("Before : row_and_col[0] is " + str(row_and_col[0]))
    print("Before : row_and_col[1] is " + str(row_and_col[1]))
    if row < 1 or row > 3:
        row_and_col[0] = 2
    if col < 1 or col > 3:
        row_and_col[1] = 2
    print("After : row_and_col[0] is " + str(row_and_col[0]))
    print("After : row_and_col[1] is " + str(row_and_col[1]))


def print_values(row, col):
    row_and_col = [row, col]
    print("row is " + str(row) + ", col is " + str(col) + ", row_and_col is " + str(row_and_col))


def handle_decimals_under_one(num_btw_zero_and_one) -> int:
    if num_btw_zero_and_one < 0.3333:
        num_btw_zero_and_one = int(1)
    elif num_btw_zero_and_one < 0.6666:
        num_btw_zero_and_one = int(2)
    else:
        num_btw_zero_and_one = int(3)
    return num_btw_zero_and_one


def replace_out_of_range(row_or_col: int) -> int:
    if row_or_col < 1 or row_or_col > 3:
        row_or_col = 4 * random()
        if row_or_col < 1:
            row_or_col = handle_decimals_under_one(row_or_col)
        else:
            row_or_col = int(row_or_col)
        return row_or_col


def return_coerced_values(row: int, col: int) -> list:
    row_and_col = [row, col]
    print("Before : row_and_col[0] is " + str(row_and_col[0]))
    print("Before : row_and_col[1] is " + str(row_and_col[1]))
    # if the input is 'out of bounds', generate a replacement using random.random()
    row_and_col[0] = replace_out_of_range(row_and_col[0])
    row_and_col[1] = replace_out_of_range(row_and_col[1])
    return row_and_col
    print("After : row_and_col[0] is " + str(row_and_col[0]))
    print("After : row_and_col[1] is " + str(row_and_col[1]))


print_values(1, 3)
coerce_values(4, 99)
rows_cols = return_coerced_values(9, 5)
print(rows_cols)
