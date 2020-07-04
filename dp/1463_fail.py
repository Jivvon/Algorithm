import sys

n = int(sys.stdin.readline())
dp = [0] * (n+1)
"""Bottom-up"""
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i%2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
    if i%3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
print(dp[n])

"""메모리 초과"""
# dq = deque([[n,depth]])
# while dq:
#     x, depth = dq.popleft()
#     if x % 2 == 0:
#         if x//2 == 1: break
#         dq.append([x//2, depth+1])
#     if x % 3 == 0:
#         if x//3 == 1: break
#         dq.append([x//3, depth+1])
#     dq.append([x-1, depth+1])
#
# print(depth+1)

"""시간 초과"""
# def dfs(depth, result):
#     global answer
#     if result == 1:
#         answer = min(answer, depth)
#         return
#     if result % 2 == 0:
#         dfs(depth+1, result // 2)
#     if result % 3 == 0:
#         dfs(depth+1, result // 3)
#     dfs(depth+1, result-1)
# dfs(0, n)
# print(answer)
