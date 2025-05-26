"""
Tic Tac Toe Player
"""

import math
import copy
from util import Node, StackFrontier, QueueFrontier

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

    num_explored = 0

    target = 0
    player_turn = player(board)
    if player_turn == X:
        target = 1
    else:
        target = -1

    start = Node(state=board, parent=None, action=None)
    frontier = QueueFrontier()
    frontier.add(start)

    explored = []
    while True:

        if frontier.empty():
            print("States Explored:", num_explored)
            return None

        node = frontier.remove()
        num_explored += 1

        if utility(node.state) == target:
            optimal_action = None
            while node.parent is not None:
                optimal_action = node.action
                node = node.parent
            print("States Explored:", num_explored)
            return optimal_action

        explored.append(node.state)

        for action, state in add_next_movement(node.state):
            if not frontier.contains_state(state) and state not in explored:
                child = Node(state=state, parent=node, action=action)
                frontier.add(child)

def add_next_movement(board):
    next_movements = []
    current_player = player(board)
    board_target = 0
    if current_player == X:
        board_target = 1
    else:
        board_target = -1

    available_actions = actions(board)
   
    for action in available_actions:
        new_board = result(board, action)
        next_movements.append((action, new_board))
        if utility(new_board) == board_target:
           return next_movements 
    
    return next_movements