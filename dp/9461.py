import sys
input = sys.stdin.readline

t = int(input())
dp = [0] + [1]*3 + [2]*2 + [0]*95
def padoban(n):
    if dp[n]:
        return dp[n]
    else:
        dp[n] = padoban(n-5) + padoban(n-1)
        return dp[n]

for _ in range(t):
    print(padoban(int(input())))
