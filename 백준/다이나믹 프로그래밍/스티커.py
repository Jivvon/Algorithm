import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    arr = [list(map(int, sys.stdin.readline().rstrip().split())) + [0, 0, 0] for _ in range(2)]

    arr[0][1] += arr[1][0]
    arr[1][1] += arr[0][0]

    for i in range(2, n):
        arr[0][i] += max(arr[1][i - 2], arr[1][i - 1])
        arr[1][i] += max(arr[0][i - 2], arr[0][i - 1])
    print(max(arr[0][n - 1], arr[1][n - 1]))

# 답은 나오는데 백준에서 IndexError
# for _ in range(t):
#     n = int(sys.stdin.readline().rstrip())
#     arr = [list(map(int, sys.stdin.readline().rstrip().split())) + [0, 0, 0] for _ in range(2)]
#     totals = []
#     for k in range(2):
#         path = [[abs(k - 1), 0]]
#         total = arr[abs(k - 1)][0]
#         for _ in range(1, n):
#             i, j = path[-1]
#             if arr[abs(i - 1)][j + 1] + arr[i][j + 2] >= arr[abs(i - 1)][j + 2]:
#                 path.append([abs(i - 1), j + 1])
#                 total += arr[abs(i - 1)][j + 1]
#             else:
#                 path.append([abs(i - 1), j + 2])
#                 total += arr[abs(i - 1)][j + 2]
#         totals.append(total)
#         print(total, "|", path)
#     answer = max(totals)
#     print(answer)
