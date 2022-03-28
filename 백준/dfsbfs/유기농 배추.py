import sys
from collections import deque


def bfs(arr, x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n, m = len(arr), len(arr[0])
    queue = deque()
    queue.append([x, y])

    while queue:
        cur_x, cur_y = queue.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if (0 <= nx < m and 0 <= ny < n) and arr[ny][nx] == 1:
                arr[ny][nx] = 0
                queue.append([nx, ny])


def solution(m, n, k):
    arr = [[0] * m for _ in range(n)]
    candidates = deque()
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        candidates.append([x, y])
        arr[y][x] = 1

    answer = 0
    while candidates:
        x, y = candidates.popleft()
        if arr[y][x] == 0:
            continue
        bfs(arr, x, y)
        answer += 1
    return answer


if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip())
    answers = []
    for _ in range(T):
        m, n, k = map(int, sys.stdin.readline().rstrip().split())
        print(solution(m, n, k))
