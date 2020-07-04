from sys import stdin

n = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

"""better"""
R, G, B = arr[0]
answer = 0
for i in range(1,n):
    R_next = arr[i][0] + min(G, B)
    G_next = arr[i][1] + min(R, B)
    B_next = arr[i][2] + min(R, G)
    answer = min([R_next,G_next,B_next])
    R, G, B = R_next,G_next,B_next
print(answer)

"""first code"""
# for i in range(1, n):
#     for j in range(3):
#         min_ = min([x for idx,x in enumerate(arr[i-1]) if j != idx])
#         arr[i][j] += min_
#
# print(min(arr[n-1]))

"""dfs"""
# cost = 1e6
# this_cost = 0
#
# def dfs(depth, prev):
#     global cost, this_cost
#     if depth == n:
#         cost = min(cost, this_cost)
#         return
#
#     for i in range(n):
#         if i == prev: continue
#         this_cost += arr[depth][i]
#         dfs(depth+1, i)
#         this_cost -= arr[depth][i]
#
# for i in range(n):
#     dfs(0, i)
#
# print(cost)
