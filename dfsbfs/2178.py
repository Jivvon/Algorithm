from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
arr = [list(map(int, list(input()[:-1]))) for _ in range(n)]
q = [(0,0)]

while q:
    this_x, this_y = q[0]
    del q[0]
    for ddx, ddy in zip(dx, dy):
        x = this_x + ddx
        y = this_y + ddy
        if 0 <= x < n and 0 <= y < m:
            if arr[x][y] == 1:
                q.append((x,y))
                arr[x][y] = arr[this_x][this_y] + 1

print(arr[n-1][m-1])

'''런타임 에러'''

# from sys import stdin
# input = stdin.readline
# from queue import Queue

# n, m = map(int, input().split())
# dx = [0, -1, 0, 1]
# dy = [1, 0, -1, 0]
# arr = [list(map(int, list(input()[:-1]))) for _ in range(n)]
# q = Queue()
# q.put((0,0))

# while not q.empty():
#     this_x, this_y = q.get()
#     for ddx, ddy in zip(dx, dy):
#         x = this_x + ddx
#         y = this_y + ddy
#         if 0 <= x < n and 0 <= y < m:
#             if arr[x][y] == 1:
#                 q.put((x, y))
#                 arr[x][y] = arr[this_x][this_y] + 1

# print(arr[n-1][m-1])

