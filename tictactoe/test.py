import tictactoe as ttt
from tictactoe import EMPTY, X, O

class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

board_X_wins = [[X, O, X],
                [O, X, O],
                [X, O, X]]
board_O_wins = [[X, O, X],
                [O, O, EMPTY],
                [X, O, X]]
board_draw =   [[X, O, X],
                [O, X, O],
                [O, X, O]]

def test(fn_name, fn):
    try:
        fn()
        print(f"{color.OKGREEN}OK{color.ENDC}       {fn_name}")
    except:
        print(f"{color.FAIL}FAILED{color.ENDC}   {fn_name}.")

def test_initial_state():
    assert ttt.initial_state() == [[EMPTY, EMPTY, EMPTY],
                                   [EMPTY, EMPTY, EMPTY],
                                   [EMPTY, EMPTY, EMPTY]]
test('initial_state', test_initial_state)

def test_player():
    board = ttt.initial_state()
    assert ttt.player(board) == X
    board = [[X, O, X],
             [O, EMPTY, O],
             [X, O, X]]
    assert ttt.player(board) == X
    board = [[X, O, X],
             [O, EMPTY, EMPTY],
             [X, O, X]]
    assert ttt.player(board) == O
    board = [[X, O, X],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, X, O]]
    assert ttt.player(board) == O
test('player', test_player)

def test_actions():
    board = ttt.initial_state()
    assert ttt.actions(board) == {(0, 0), (0, 1), (0, 2),
                                  (1, 0), (1, 1), (1, 2),
                                  (2, 0), (2, 1), (2, 2)}
    board[0][0] = X
    board[0][1] = O
    assert ttt.actions(board) == {(0, 2),
                                  (1, 0), (1, 1), (1, 2),
                                  (2, 0), (2, 1), (2, 2)}
    board[2][1] = X
    assert ttt.actions(board) == {(0, 2),
                                  (1, 0), (1, 1), (1, 2),
                                  (2, 0), (2, 2)}
    
    
test('actions', test_actions)

def test_result():
    board = ttt.initial_state()
    board = ttt.result(board, (0, 0))
    assert board == [[X, EMPTY, EMPTY],
                          [EMPTY, EMPTY, EMPTY],
                          [EMPTY, EMPTY, EMPTY]]
    board = ttt.result(board, (1, 1))
    assert board == [[X, EMPTY, EMPTY],
                          [EMPTY, O, EMPTY],
                          [EMPTY, EMPTY, EMPTY]]
    board = ttt.result(board, (2, 2))
    assert board == [[X, EMPTY, EMPTY],
                          [EMPTY, O, EMPTY],
                          [EMPTY, EMPTY, X]]
test('result', test_result)

def terst_winner():
    board = ttt.initial_state()
    assert ttt.winner(board) == None
    assert ttt.winner(board_X_wins) == X
    assert ttt.winner(board_O_wins) == O
    assert ttt.winner(board_draw) == None
test('winner', terst_winner)

def test_terminal():
    board = ttt.initial_state()
    assert ttt.terminal(board) == False
    assert ttt.terminal(board_X_wins) == True
    assert ttt.terminal(board_O_wins) == True
    assert ttt.terminal(board_draw) == True
test('terminal', test_terminal)

def test_utility():
    board = ttt.initial_state()
    assert ttt.utility(board) == 0
    assert ttt.utility(board_X_wins) == 1
    assert ttt.utility(board_O_wins) == -1
    assert ttt.utility(board_draw) == 0
test('utility', test_utility)

def test_minimax():
    # board = ttt.initial_state()
    # assert ttt.minimax(board) == (0, 1)
    board = [[X, O, X],
             [O, X, O],
             [O, X, EMPTY]]
    assert ttt.minimax(board) == (2, 2)
    board = [[X, O, X],
             [O, EMPTY, O],
             [X, O, X]]
    assert ttt.minimax(board) == (1, 1)
    board = [[X, O, X],
             [O, O, EMPTY],
             [X, EMPTY, X]]
    assert ttt.minimax(board) == (1, 2)
    board = board_draw
    assert ttt.minimax(board) == None
test('minimax', test_minimax)
