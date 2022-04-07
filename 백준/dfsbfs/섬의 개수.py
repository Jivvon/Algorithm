import sys
from collections import deque


def bfs(arr, x, y, w, h):
    queue = deque()
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    queue.append([x, y])
    arr[y][x] = 0

    while queue:
        cur_x, cur_y = queue.popleft()
        arr[cur_y][cur_x] = 0
        for i in range(8):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if (0 <= nx < w and 0 <= ny < h) and \
                    arr[ny][nx] == 1:
                arr[ny][nx] = 0
                queue.append([nx, ny])


if __name__ == '__main__':
    while True:
        w, h = map(int, sys.stdin.readline().rstrip().split())
        if w == h == 0:
            break
        board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h)]
        answer = 0
        for i in range(h):
            for j in range(w):
                if board[i][j] == 1:
                    bfs(board, j, i, w, h)
                    answer += 1
        print(answer)
