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
    #TODO Use enumerate instead of board_index and row_index
    available_Actions = set()

    board_index = 0
    for row in board :
        row_index = 0
        for cell in row:
            if cell == EMPTY:
                available_Actions.add((board_index, row_index))
            row_index += 1
        board_index += 1
    return available_Actions


def result(board, action):
    if action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise Exception("Invalid action")
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid action")
    new_Board = copy.deepcopy(board)
    player_Turn = player(board)
    new_Board[action[0]][action[1]] = player_Turn
    return new_Board


def winner(board):
    # TODO Use enumerate instead of board_index and row_index
    columns = [0,0,0]
    cross_0 = 0
    cross_1 = 0
    board_index = 0
    for row in board :
        row_Value = 0
        row_index = 0

        for cell in row:
            cell_Value = 0
            if cell == EMPTY:
                cell_Value += 0
            elif cell == X:
                cell_Value += 1
            elif cell == O:
                cell_Value += -1

            if (0,0) == (board_index, row_index):
                cross_0 += cell_Value
            elif (0,2) == (board_index, row_index):
                cross_1 += cell_Value
            elif (1,1) == (board_index, row_index):
                cross_0 += cell_Value
                cross_1 += cell_Value
            elif (2,0) == (board_index, row_index):
                cross_1 += cell_Value
            elif (2,2) == (board_index, row_index):
                cross_0 += cell_Value    

            columns[row_index] += cell_Value
            row_Value += cell_Value
            row_index += 1  

        if row_Value == 3:
            return X
        elif row_Value == -3:   
            return O
        board_index += 1       

    if columns[0] == 3 or columns[1] == 3 or columns[2] == 3:
        return X
    elif columns[0] == -3 or columns[1] == -3 or columns[2] == -3:
        return O
    
    if cross_0 == 3 or cross_1 == 3:
        return X
    elif cross_0 == -3 or cross_1 == -3:
        return O

    return None


def terminal(board):
    empty_Count = sum(cell == EMPTY for row in board for cell in row)
    if empty_Count == 0 or winner(board) is not None:
        return True
    else:
        return False

def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None
    if player(board) == X:
        action = minimax_value(None, board, True)
        return action[0]
    else:
        action = minimax_value(None, board, False)
        return action[0]

def minimax_value(initial_action, board, is_max_player):
    if terminal(board):
        return (initial_action, utility(board))
    
    if is_max_player:
        max_Eval = -math.inf
        max_Action = None
        for action in actions(board):
            eval = minimax_value(action, result(board, action), False)
            if eval[1] > max_Eval:
                max_Eval = eval[1]
                max_Action = eval[0]
        return (max_Action, max_Eval)
    else:
        min_Eval = math.inf
        min_Action = None
        for action in actions(board):
            eval = minimax_value(action, result(board, action), True)
            if eval[1] < min_Eval:
                min_Eval = eval[1]
                min_Action = eval[0]
        return (min_Action, min_Eval)