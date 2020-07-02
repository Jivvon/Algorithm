import sys
input = sys.stdin.readline

N = int(input())
answer = 0
col, diag_l, diag_r = [False] * N, [False] * (2*N-1), [False] * (2*N-1)

def dfs(depth):
    global answer
    if depth == N:
        answer += 1
        return
    for i in range(N):
        if not (col[i] or diag_l[i+depth] or diag_r[i-depth+N-1]):
            col[i] = diag_l[i+depth] = diag_r[i-depth+N-1] = True
            dfs(depth+1)
            col[i] = diag_l[i+depth] = diag_r[i-depth+N-1] = False

dfs(0)
print(answer)
