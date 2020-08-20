from sys import stdin
input = stdin.readline
from collections import deque

N, M, H = map(int, input().split())
arr = [[list(map(int,input()[:-1].split())) for _ in range(M)] for __ in range(H)]
dx, dy, dz = [0, -1, 0, 1, 0, 0], [1, 0, -1, 0, 0, 0],[0, 0, 0, 0, 1, -1]
queue = deque()

for i in range(N):
    for j in range(M):
        for k in range(H):
            if arr[k][j][i] == 1:
                queue.append((k,j,i))

while queue:
    this_z, this_y, this_x = queue.popleft()
    for i in range(6):
        x, y, z = this_x + dx[i], this_y + dy[i], this_z + dz[i]
        if 0 <= x < N and 0 <= y < M and 0 <= z < H:
            if arr[z][y][x] == 0:
                arr[z][y][x] = arr[this_z][this_y][this_x] + 1
                queue.append((z,y,x))

answer = 0
for j in range(M):
    for k in range(H):
        if 0 in arr[k][j]:
            print(-1)
            exit(0)
        answer = max(answer, max(arr[k][j]))
    
print(answer - 1)