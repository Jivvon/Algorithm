# 68ms

import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []
arr = list(map(int, input().split()))

for el in arr:
    heapq.heappush(h, el)

answer = sum([len(h) * heapq.heappop(h) for _ in range(n)])
print(answer)
