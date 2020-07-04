# 시간초과, 메모리 초과 뜬다
# 그냥 dfs 구현해서 풀었다
import sys, itertools
input = sys.stdin.readline
N, M = map(int, input().split())

arr = list(itertools.product(range(1, N+1), repeat=M))

def func(i):
    for j in range(M-1):
        if i[j] > i[j+1]:
            return False
    return True

arr = filter(func,arr)

for i in arr:
    print(*i)
