with open('test_input_4.txt', 'r') as f:
    inp = f.read()

num, *boards = inp.split('\n\n')

nums = [int(x) for x in num.split(',')]
allBoards = [[[int(x) for x in row.split()] for row in board.split('\n')] for board in boards[:-1]]

def n_finder_in_board(board,n):
    for r in range(5):
        for c in range(5):
            if board[r][c] == n:
                board[r][c] = 'x'
    return board


def check(board):
    ans = False
    for i in board:
        while not ans:
            if all(x == 'x' for x in i):
                ans = True
            elif any(x == 'x' for x in i):
                if all(board[i.index('x')][j] for j in range(5)):
                    ans = True
    return ans


def sum_of_all_rested_numbers(board):
    sc = 0
    for r in range(5):
        for c in range(5):
            if board[r][c] != 'x':
                sc += board[r][c]
    return sc


for n in num:
    for board in allBoards:
        board = n_finder_in_board(board,n)
        if check(board):
            print(board)
            print(n*sum_of_all_rested_numbers(board))
