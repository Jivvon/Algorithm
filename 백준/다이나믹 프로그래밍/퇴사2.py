import sys

n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dp = [0] * (n + 1)

m = 0
for i in range(n):
    m = max(m, dp[i])
    if i + arr[i][0] > n:
        continue
    dp[i + arr[i][0]] = max(m + arr[i][1], dp[i + arr[i][0]])
print(max(dp))

# 시간 초과
# for idx, a in enumerate(arr):
#     arr[idx] = [idx, idx + a[0] - 1, a[1]]
# arr.sort(key=lambda x: (x[1], x[0]))
#
# dp = [0] * n
# for i in range(n):
#     cur = 0
#     for start, _, profit in list(filter(lambda x: x[1] == i, arr)):
#         cur = max(cur, dp[start - 1] + profit)
#     dp[i] = cur
#     if i > 0 and dp[i] == 0:
#         dp[i] = dp[i - 1]
#
# print(dp[-1])
