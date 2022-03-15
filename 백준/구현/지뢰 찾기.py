"""
지뢰가 없으면서 열린 칸에는 0과 8 사이의 숫자가 있어야 한다.
지뢰가 있는 칸이 열렸다면 지뢰가 있는 모든 칸이 별표(*)로 표시되어야 한다.
다른 모든 지점은 온점(.)이어야 한다.
"""

import sys


def near_bombs(n, bombs, x, y):
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    count = 0
    for _dx, _dy in zip(dx, dy):
        nx = x + _dx
        ny = y + _dy
        if (0 <= nx < n and 0 <= ny < n) \
                and [nx, ny] in bombs:
            count += 1

    return count


def do_game(n, board, bombs):
    for i in range(n):
        for j in range(n):
            if board[i][j] == "x":
                board[i][j] = str(near_bombs(n, bombs, i, j))

    for bomb in bombs:
        if "0" <= board[bomb[0]][bomb[1]] <= "9":
            for _bomb in bombs:
                board[_bomb[0]][_bomb[1]] = "*"
            break


def solution():
    n = int(sys.stdin.readline().rstrip())
    bombs = []
    for i in range(n):
        tmp = list(sys.stdin.readline().rstrip())
        for j, _ in filter(lambda x: x[1] == "*", enumerate(tmp)):
            bombs.append([i, j])
    board = []
    for i in range(n):
        board.append(list(sys.stdin.readline().rstrip()))
    do_game(n, board, bombs)

    for b in board:
        print(''.join(b))


if __name__ == '__main__':
    solution()
