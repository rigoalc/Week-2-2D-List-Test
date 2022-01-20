from create_board import create_board
from create_board import EXPECTED
def test_create_board():
    board = [
        ['*', '*', '*'],
        ['*', '*', '*'],
        ['*', '*', '*'],
    ]
    board = create_board(board)
    assert board == EXPECTED