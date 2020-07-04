from sys import stdin

t = int(stdin.readline())
dp = [1, 1, 1, 2, 2]
max_ = 0
ns = []

for _ in range(t):
    ns.append(int(stdin.readline()))
    max_ = max(ns[-1],max_)

for i in range(5, max_):
    dp.append(dp[-1]+dp[-5])

for i in ns:
    print(dp[i-1])
