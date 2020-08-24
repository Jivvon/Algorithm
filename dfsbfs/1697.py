'''1 등 코드'''
def c(n, k):
    if n >= k:
        return n - k
    elif k == 1:
        return 1
    elif k % 2:
        return 1 + min(c(n, k - 1), c(n, k + 1))
    else:
        return min(k-n, 1+c(n, k//2))
n, k = map(int, input().split())
print(c(n,k))
# '''BETTER'''
# from sys import stdin
# from collections import deque
# input = stdin.readline

# n, k = map(int, input().split())
# maxSize = 100001
# position = [0] * maxSize
# queue = deque()

# def solve(arr, n, k):
#     queue.append(n)

#     while queue:
#         i = queue.popleft()
#         if i == k:
#             return arr[i]
#         for j in (i + 1, i - 1, i * 2):
#             if 0 <= j < maxSize and (arr[j] == 0 or arr[i] + 1 < arr[j]):
#                 arr[j] = arr[i] + 1
#                 queue.append(j)

# print(solve(position, n, k))

# '''GOOD'''
# from sys import stdin
# from collections import deque
# input = stdin.readline

# n, k = map(int, input().split())
# maxSize = 100001
# position = [0] * maxSize
# queue = deque([n])

# def move(cur, nex):
#     if (0 <= nex < maxSize) and \
#         (position[nex] == 0 or position[cur] + 1 < position[nex]):
#         position[nex] = position[cur] + 1
#         queue.append(nex)

# def solve():
#     while queue:
#         cur = queue.popleft()
#         if cur == k:
#             return position[cur]
#         move(cur, cur - 1)
#         move(cur, cur + 1)
#         move(cur, cur * 2)

# print(solve())