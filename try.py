# def board_checker(board):
#     for r in range(len(board)):
#         if all(el == 'x' for el in board[r]):
#             return True
#         elif 'x' in board[r]:
#             c = board[r].index('x')
#             print(c)
#             if all(board[r][c] == 'x' for r in range(len(board))):
#                 return True
#         else:
#             return False

def check(board):
    ans = True
    while ans:
        for i in board:
            if all(x == 'x' for x in i):
                print(i)
                ans = False
                break
            elif any(x == 'x' for x in i):
                print(i)
                print(i.index('x'))
                if all(board[j][i.index('x')] == 'x' for j in range(5)):
                    print([board[j][i.index('x')] for j in range(5)])
                    print('col')
                    ans = False
                    break
    return ans

a = [[3, 'x', 'x', 'x', 1], [3, 2, 'x', 'x', 'x'], ['x', 91, 54, 13, 'x'], ['x', 88, 75, 99, 'x'], ['x', 31,  4,  0, 'x']]

print(check(a))
