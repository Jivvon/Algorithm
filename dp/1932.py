import sys
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

"""bottom-up"""
for i in range(n-1, 0, -1):
    for j in range(len(arr[i])-1):
        if arr[i][j] > arr[i][j+1]:
            arr[i-1][j] += arr[i][j]
        else:
            arr[i-1][j] += arr[i][j+1]

print(arr[0][0])

"""top-down"""
# for i in range(1, n):
#     for j in range(len(arr[i])):
#         if j == 0:
#             arr[i][j] += arr[i-1][0]
#         elif j == i:
#             arr[i][j] += arr[i-1][j-1]
#         else:
#             arr[i][j] += max(arr[i-1][j-1:j+1])
#
# print(max(arr[n-1]))
