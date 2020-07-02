import sys
input = sys.stdin.readline

N, M = map(int, input().split())

visited = [False] * (N+1)
answer = []
def dfs(depth):
    if depth == M:
        print(' '.join(answer))
        return
    for i in range(1, N+1):
        answer.append(str(i))
        dfs(depth+1)
        answer.pop()
dfs(0)
