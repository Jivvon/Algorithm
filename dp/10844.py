from sys import stdin
n = int(stdin.readline())
dp = {}
for i in range(1, n+1): # 1 ~ n
    dp[i] = [0]*11 # 0 ~ 10, 10은 prev가 0이나 9일 때의 바깥 값 (리스트에서 [-1]은 마지막 요소)

for i in range(1, 10): # 1 ~ 9
    dp[1][i] = 1 # n이 1일 때

for i in range(2, n+1):
    for j in range(10):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000) # 정답
# print(int(sum(dp[n]) % 1e9)) # 오답
