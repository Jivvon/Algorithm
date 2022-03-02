import sys

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, list(sys.stdin.readline().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    from collections import deque
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]
            if (0 <= nx < N and 0 <= ny < M) and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1


bfs()
print(graph[N - 1][M - 1])
