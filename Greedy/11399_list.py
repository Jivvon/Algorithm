# 64ms

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr, reverse=True)

answer = sum([len(arr) * arr.pop() for _ in range(n)])
print(answer)
