'''백준에서 exit(0) 사용하자
    exit(1)과 exit(-1)은 런타임 에러가 발생한다.'''

from sys import stdin
input = stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int,input()[:-1].split())) for _ in range(M)]
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
queue = deque()

for j in range(N):
    for i in range(M):
        if arr[i][j] == 1:
            queue.append((i,j))

while queue:
    this_x, this_y = queue.popleft()
    for ddx, ddy in zip(dx, dy):
        x, y = this_x + ddx, this_y + ddy
        if 0 <= x < M and 0 <= y < N:
            if arr[x][y] == 0:
                arr[x][y] = arr[this_x][this_y] + 1
                queue.append((x, y))

answer = 0
for i in range(M):
    for j in range(N):
        answer = max(answer, arr[i][j])
        if arr[i][j] == 0:
            print(-1)
            exit(0)

print(answer - 1)

'''런타임 에러'''
# 시간 초과 코드에서 list.pop(0)을 list.pop()으로 바꿈.
'''list.pop(0)은 첫 번째 요소를 pop한 후 나머지 요소를 앞으로 한 칸씩 당기므로
    O(N)의 시간이 걸린다.'''

'''시간 초과'''

# from sys import stdin
# input = stdin.readline

# N, M = map(int, input().split())
# arr = [input()[:-1].split() for _ in range(M)]
# dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
# queue = []
# answer = 0

# for j in range(N):
#     for i in range(M):
#         if arr[i][j] == '1':
#             queue.append((i,j))

# while queue:
#     queue_tmp = []
#     while queue:
#         this_x, this_y = queue.pop(0)
#         for ddx, ddy in zip(dx, dy):
#             x, y = this_x + ddx, this_y + ddy
#             if 0 <= x < M and 0 <= y < N:
#                 if arr[x][y] == '0':
#                     arr[x][y] = '1'
#                     queue_tmp.append((x, y))
#     queue = queue_tmp
#     answer += 1

# for j in range(N):
#     for i in range(M):
#         if arr[i][j] == '0':
#             print(-1)
#             exit(-1)

# print(answer-1)