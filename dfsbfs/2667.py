import sys

# 방향 좌, 상, 우, 하
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N = int(sys.stdin.readline())
mat = [list(sys.stdin.readline()[:-1]) for _ in range(N)]
cnt = 0
apt = []

def dfs(x,y):
    global cnt
    mat[x][y] = '0'
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if mat[nx][ny] == '1':
            dfs(nx,ny)

for i in range(N):
    for j in range(N):
        if mat[i][j] == '1':
            cnt = 0
            dfs(i,j)
            apt.append(cnt)

print(len(apt))
apt.sort()
for i in apt:
    print(i)
