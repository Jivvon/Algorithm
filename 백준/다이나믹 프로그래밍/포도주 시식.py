import sys

input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]

if n == 1 or n == 2:
    print(sum(arr))
else:
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = sum(arr[0:2])
    dp[2] = max(sum(arr[0:3:2]), sum(arr[0:2]), sum(arr[1:3]))

    for i in range(3, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i])

    print(dp[-1])
