import getopt
import signal
import sys
#
# Python 3
#
from typing import List


class Move:
    def __init__(self, player_index, col, row):
        self.player_index = player_index
        self.col = col
        self.row = row


def winning_player_index(board, last_move):
    """
    TODO:  implement!
    This function is called after every move, which means that if it is being
    called, a win has not previously been detected.
    :param board: 2-dimensional array of integers containing player indexes
    :param last_move: Move object representing the last move made
    :return: player_index of winner; or -1 if no winner detected
    """

    def is_player_cell(board: List[List[int]], row: int, col: int) -> bool:
        if row >= len(board) or col >= len(board[row]):
            return False
        if board[row][col] != last_move.player_index:
            return False

        return True

    def check_vertical(board: List[List[int]], last_move: Move) -> bool:
        counter = 1

        row = last_move.row + 1
        while is_player_cell(board, row, last_move.col):
            row += 1
            counter += 1

        row = last_move.row - 1
        while is_player_cell(board, row, last_move.col):
            row -= 1
            counter += 1

        if counter >= 4:
            return True

        return False

    def check_horizontal(board: List[List[int]], last_move: Move) -> bool:
        counter = 1

        col = last_move.col + 1
        while is_player_cell(board, last_move.row, col):
            col += 1
            counter += 1

        col = last_move.col - 1
        while is_player_cell(board, last_move.row, col):
            col -= 1
            counter += 1

        if counter >= 4:
            return True

        return False

    def check_forward_slash(board: List[List[int]], last_move: Move) -> bool:
        counter = 1

        col = last_move.col + 1
        row = last_move.row - 1
        while is_player_cell(board, row, col):
            col += 1
            row -= 1
            counter += 1

        col = last_move.col - 1
        row = last_move.row + 1
        while is_player_cell(board, row, col):
            col -= 1
            row += 1
            counter += 1

        if counter >= 4:
            return True

        return False

    def check_backward_slash(board: List[List[int]], last_move: Move) -> bool:
        counter = 1

        col = last_move.col + 1
        row = last_move.row + 1
        while is_player_cell(board, row, col):
            col += 1
            row += 1
            counter += 1

        col = last_move.col - 1
        row = last_move.row - 1
        while is_player_cell(board, row, col):
            col -= 1
            row -= 1
            counter += 1

        if counter >= 4:
            return True

        return False

    if check_vertical(board, last_move):
        return last_move.player_index
    if check_horizontal(board, last_move):
        return last_move.player_index
    if check_forward_slash(board, last_move):
        return last_move.player_index
    if check_backward_slash(board, last_move):
        return last_move.player_index

    return -1


##### PREDEFINED FUNCTIONS #####

def is_valid_move(board, move):
    """
    Checks if move is valid
    :param board: 2-dimensional array of integers containing player indexes
    :param move: Move object representing the move to validate
    :return: boolean if move is valid given board
    """

    # check min boundary violations
    if move.row < 0 or move.col < 0:
        return False

    # check max boundary violations
    if move.row >= len(board) or move.col >= len(board[0]):
        return False

    # can't place over existing piece
    if board[move.row][move.col] > -1:
        return False

    # TODO What is this???
    # check that we are stacking if not on bottom row
    # if move.row < len(board) - 1 and board[move.row + 1][move.col] < 0:
    #     return False

    return True


def update_board(board, move):
    """
    Update board with move.
    :param board: 2-dimensional array of integers containing player indexes
    :param move: Move object representing the move to update on board
    :return:
    """
    board[move.row][move.col] = move.player_index


def parse_move(player_index, move_input):
    tokens = move_input.split(',', 2)
    if len(tokens) != 2:
        return None
    # tokens[0] = tokens[0].s1trip()
    if not tokens[0].strip().isdigit() or not tokens[1].strip().isdigit():
        return None
    col = int(tokens[0].strip()) - 1
    row = int(tokens[1].strip()) - 1
    move = Move(player_index, col, row)
    print('Player #{} places piece in ({},{})'.format(player_index + 1, col + 1, row + 1))
    return move


def exit_script():
    print('\n\nExiting...\n\n')
    sys.exit(0)


def sigint_handler(signal, frame):
    exit_script()


def prompt_str_val(prompt):
    print
    while (True):
        choice = input(prompt)
        choice = choice.strip()
        if (len(choice) > 0):
            return choice


def print_board(board, player_symbols):
    print()
    print('    ', end='')
    for col_index in range(len(board[0])):
        print("{:>3} ".format(col_index + 1), end='')
    print()
    for row_index in range(len(board)):
        row = board[row_index]
        print("{:>3} ".format(row_index + 1), end='')
        for col in range(len(row)):
            player_symbol = '.'
            player_index = board[row_index][col]
            if player_index >= 0:
                player_symbol = player_symbols[player_index]
            print("{:>3} ".format(player_symbol), end='')
        print()
    print()


##### MAIN #####
if __name__ == '__main__':
    ##### COMMAND-LINE ARGS #####

    ROWS = 6
    COLS = 7
    HUMANS = 2
    ROBOTS = 0

    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["rows=", "cols=", "humans=", "robots="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        sys.exit(2)

    for o, a in opts:
        if o in ("--rows"):
            assert a.isdigit(), a + ' is not a valid option for rows.'
            ROWS = int(a)
        elif o in ("--cols"):
            assert a.isdigit(), a + ' is not a valid option for cols.'
            COLS = int(a)
        elif o in ("--humans"):
            assert a.isdigit(), a + ' is not a valid option for humans.'
            HUMANS = int(a)
        elif o in ("--robots"):
            assert a.isdigit(), a + ' is not a valid option for robots.'
            ROBOTS = int(a)
        else:
            assert False, "Unhandled option:  " + o

    print(
        '\n>>>>> Board = {} rows x {} cols; Human Players = {}; Robot Players = {}'.format(ROWS, COLS, HUMANS, ROBOTS))
    PLAYERS = HUMANS + ROBOTS

    # catch ctrl-c
    signal.signal(signal.SIGINT, sigint_handler)

    # map player_index to a symbol so board is easier to view
    PLAYER_SYMBOLS = ['X', 'O', 'A', 'B', 'C', 'D', 'E', 'Y', 'Z', 'H']

    # initialize board
    board = [[-1 for cols in range(COLS)] for rows in range(ROWS)]

    # main terminal interface loop
    move_count = 0
    while True:
        for player_index in range(PLAYERS):
            display_player_id = player_index + 1
            print_board(board, PLAYER_SYMBOLS)

            while True:
                move_input = prompt_str_val("Player #{} Move (col, row):  ".format(display_player_id))
                move = parse_move(player_index, move_input)
                if move is not None and is_valid_move(board, move):
                    update_board(board, move)
                    move_count += 1
                    break
                else:
                    print("INVALID MOVE")

            if winning_player_index(board, move) > -1:
                print_board(board, PLAYER_SYMBOLS)
                print('\n\nPlayer #{} wins!\n\n'.format(display_player_id))
                exit_script()

            if move_count == (ROWS * COLS):
                print_board(board, PLAYER_SYMBOLS)
                print("\n\nIt's a draw!")
                exit_script()
