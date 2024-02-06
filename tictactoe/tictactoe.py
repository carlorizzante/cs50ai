"""
Tic Tac Toe Player
"""

import copy
import math

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
    """
    Returns player who has the next turn on a board.
    """
    count_empty = 0
    for row in board:
        for cell in row:
            if cell == EMPTY:
                count_empty += 1
    if count_empty % 2 == 0:
        # print(count_empty, 'O')
        return O
    else:
        # print(count_empty, 'X')
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2] != None:
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2] != None:
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2] != None:
        return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0] != None:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] != None:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] != None:
        return board[0][2]
    elif board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) != None) or (not any(EMPTY in sublist for sublist in board)):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if (terminal(board)):
        return None
    if player(board) == X:
        _, move = max_value(board)
        return move
    else:
        _, move = min_value(board)
        return move


def max_value(board):
    """
    Returns the max value of the board and the best move.
    """
    if terminal(board):
        return utility(board), None
    v = -math.inf
    move = None
    for action in actions(board):
        new_v, _ = min_value(result(board, action))
        if new_v > v:
            v = new_v
            move = action
    return v, move


def min_value(board):
    """
    Returns the min value of the board and the best move.
    """
    if terminal(board):
        return utility(board), None
    v = math.inf
    move = None
    for action in actions(board):
        new_v, _ = max_value(result(board, action))
        if new_v < v:
            v = new_v
            move = action
    return v, move
