import copy
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(arr, x, y, h):
    queue = deque()
    queue.append([x, y])
    arr[y][x] = -1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n and 0 <= ny < n) and arr[ny][nx] > h:
                arr[ny][nx] = -1
                queue.append([nx, ny])


answer = 1
nums = set(sum(board, []))

for h in nums:
    arr = copy.deepcopy(board)
    count = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > h:
                bfs(arr, j, i, h)
                count += 1
    answer = max(answer, count)

print(answer)
