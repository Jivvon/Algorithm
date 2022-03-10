import sys

num_board = dict()
for i in range(5):
    for j, val in enumerate(list(map(int, sys.stdin.readline().rstrip().split()))):
        num_board[val] = [i, j]


def bingo_total(board):
    count = 0
    for row in board:
        if sum(row) == 5:
            count += 1
    for col in zip(*board):
        if sum(col) == 5:
            count += 1
    if sum([board[i][i] for i in range(5)]) == 5:
        count += 1
    if sum([board[i][4 - i] for i in range(5)]) == 5:
        count += 1
    return count


def solution(num_board):
    count = 0
    bingo_board = [[0] * 5 for _ in range(5)]

    for _ in range(5):
        for _, val in enumerate(list(map(int, sys.stdin.readline().rstrip().split()))):
            i, j = num_board.pop(val)
            bingo_board[i][j] = 1

            count += 1
            if bingo_total(bingo_board) >= 3:
                return count


answer = solution(num_board)
print(answer)
