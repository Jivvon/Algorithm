# 다시 풀어보자....

import sys
input = sys.stdin.readline
blanks = {}
blanks_list = []
board = []
nums = set(range(1,10))

def init():
    for j in range(9):
        row = list(map(int, input().split()))
        for i, v in enumerate(row):
            if v == 0:
                blanks[(i, j)] = nums.copy()
        board.append(row)

def check(x, y):
    min_x = (x // 3)*3
    min_y = (y // 3)*3
    row = set(board[y])
    col = set([board[y][k] for k in range(9)])
    box = set([board[j][i] for j in range(min_y, min_y+3) for i in range(min_x, min_x+3)])

    candidates = blanks[(x, y)]

    candidates -= row
    candidates -= col
    candidates -= box

    return candidates

flag = False
def dfs(depth):
    global flag, blanks_list
    if flag : return
    if depth == len(blanks_list):
        for li in board:
            print(*li)
        flag = True
        return

    candidates = check(*blanks_list[depth])

    for candidate in candidates:
        board[blanks_list[depth][1]][blanks_list[depth][0]] = candidate
        dfs(depth+1)
        board[blanks_list[depth][1]][blanks_list[depth][0]] = 0

init()
for key in blanks.keys():
    blanks[key] = check(*key)

remove_key = []
for (x, y) in blanks:
    if len(check(x, y)) == 1:
        board[y][x] = blanks[(x, y)].pop()
        remove_key.append((x, y))
for key in list(blanks.keys()):
    if key in remove_key:
        del blanks[key]
blanks_list = list(blanks)
dfs(0)
