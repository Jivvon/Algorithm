import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
dp = [0, 1] + [-1] * 89

def fibo(n):
    if dp[n] != -1:
        return dp[n]
    dp[n] = fibo(n-2) + fibo(n-1)
    return dp[n]

n = int(input())
print(fibo(n))
