def create_board(board):
    # TODO: do what problem asks
        # Doing just the first column for now
    board[0][0] = 'X'
    board[1][0] = 'O'
    board[2][0] = 'X'
    
    return board
    

EXPECTED = [
    ['X', 'O', 'O'],
    ['O', 'X', 'X'],
    ['X', 'X', 'O'],
]

