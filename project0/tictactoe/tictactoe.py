"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    empty_Count = sum(cell == EMPTY for row in board for cell in row)
    if empty_Count % 2:
        return X
    else:
        return O

def actions(board):
    available_Actions = set()

    for row in board :
        for cell in row:
            if cell == EMPTY:
                available_Actions.add((board.index(row), row.index(cell)))
    return available_Actions


def result(board, action):
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid action")
    new_Board = copy.deepcopy(board)
    player_Turn = player(board)
    new_Board[action[0]][action[1]] = player_Turn
    return new_Board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    collum_0 = 0
    collum_1 = 0
    collum_2 = 0
    cross_0 = 0
    cross_1 = 0
    for row in board :
        row_Value = 0
        for cell in row:
            if cell == EMPTY:
                row_Value += 0
            elif cell == X:
                row_Value += 1
            elif cell == O:
                row_Value += -1
        if row_Value == 3:
            return X
        elif row_Value == -3:   
            return O       
                            
    return None


def terminal(board):
    empty_Count = sum(cell == EMPTY for row in board for cell in row)
    if empty_Count == 0:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                return (i, j)
        else:
            continue
    return None

