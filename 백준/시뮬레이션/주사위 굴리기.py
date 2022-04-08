import sys

n, m, y, x, _ = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
commands = list(map(int, sys.stdin.readline().rstrip().split()))  # 1~4 = 동 서 북 남

dice = [0] * 6
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
arrs = [[0, 3, 1, 5],
        [0, 5, 1, 3],
        [0, 2, 1, 4],
        [0, 4, 1, 2]]

for comm in commands:
    cur_d = comm - 1
    nx = x + dx[cur_d]
    ny = y + dy[cur_d]
    if not (0 <= nx < m and 0 <= ny < n):
        continue
    if board[y][x] == 0:
        board[y][x] = dice[1]
    else:
        dice[1] = board[y][x]
        board[y][x] = 0

    prev = dice[arrs[cur_d][-1]]
    for a in arrs[cur_d]:
        prev, dice[a] = dice[a], prev
    x, y = nx, ny
    print(dice[0])
