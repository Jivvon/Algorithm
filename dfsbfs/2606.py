import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
mat = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, m+1):
    a, b = list(map(int, sys.stdin.readline().split()))
    mat[a][b] = mat[b][a] = 1

def dfs(v, visited, stack):
    stack += [v]
    visited += [v]
    for i in range(1, n+1):
        if i not in visited and mat[v][i] == 1:
            dfs(i, visited, stack)
    stack.remove(v)
    return len(visited)-1

print(dfs(1, [], []))

