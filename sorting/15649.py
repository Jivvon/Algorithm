N, M = map(int, input().split())

visited = [False] * N
ret = []
def dfs(depth, N, M):
    if depth == M:
        print(' '.join(map(str, ret)))
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            ret.append(i+1)
            dfs(depth+1, N, M)
            visited[i] = False
            ret.pop()

dfs(0, N, M)
