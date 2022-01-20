def create_board(board):
    # TODO: do what problem asks
    return board

EXPECTED = [
    ['X', 'O', 'O'],
    ['O', 'X', 'X'],
    ['X', 'X', 'O'],
]

def test_create_board():
    board = [
        ['*', '*', '*'],
        ['*', '*', '*'],
        ['*', '*', '*'],
    ]
    board = create_board(board)
    assert board == EXPECTED