import os
import sys

N = int(input())
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, list(sys.stdin.readline())[:-1]))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answers = []
count = 0


def dfs(graph, x, y, N):
    global count
    if x < 0 or y < 0 or x >= N or y >= N:
        return
    if graph[x][y] != 0:
        graph[x][y] = 0
        count += 1
        for i in range(4):
            dfs(graph, x + dx[i], y + dy[i], N)


for x in range(N):
    for y in range(N):
        count = 0
        dfs(graph, x, y, N)
        if count > 0:
            answers.append(count)

print(len(answers))
print(os.linesep.join(map(str, sorted(answers))))
