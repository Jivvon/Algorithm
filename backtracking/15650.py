import sys, itertools
def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
# for _ in itertools.combinations(range(1, N+1), M):
#     print(*_)

visited = [False] * (N+1)
arr = []
def dfs(depth, index):
    if depth == M:
        print(' '.join(arr))
        return

    for i in range(index, N+1):
        if not visited[i]:
            visited[i] = True
            arr.append(str(i))
            dfs(depth+1, i+1)
            arr.pop()
            visited[i] = False
    return
dfs(0, 1)
