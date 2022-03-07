n = int(input())
dp = [0, 1, 2, 4, 7]

for _ in range(n):
    k = int(input())
    if k < len(dp):
        print(dp[k])
        continue
    for i in range(len(dp), k + 1):
        dp.append(sum(dp[i - 3:i]))
    print(dp[k])
