def test_create_board():
    board = [
        ['*', '*', '*'],
        ['*', '*', '*'],
        ['*', '*', '*'],
    ]
    board = create_board(board)
    assert board == EXPECTED