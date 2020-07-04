import sys

n, m, v = list(map(int, sys.stdin.readline().split()))
mat = [[0] * (n+1) for _ in range(n+1)] # 인접행렬

# 간선
for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    mat[a][b] = mat[b][a] = 1

visited = [0] * (n+1)

def dfs(v):
    print(v, end=' ')
    visited[v] = 1
    for i in range(1, n+1):
        if visited[i] == 0 and mat[v][i] == 1:
            dfs(i)

visited = [0] * (n+1)

def bfs(v):
    queue = [v]
    visited[v] = 1
    while queue:
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, n+1):
            if visited[i] == 0 and mat[v][i] == 1:
                queue.append(i)
                visited[i] = 1

dfs(v)
visited = [0] * (n+1)
print()
bfs(v)
