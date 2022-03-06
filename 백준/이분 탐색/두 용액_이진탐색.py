# 이진탐색

import sys

input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
min_s = 1 << 31

if n == 2:
    print(*arr)
    exit(0)

for i in range(n - 1):
    start = i + 1
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        s = arr[i] + arr[mid]

        if abs(s) < min_s:
            idx1, idx2, min_s = i, mid, abs(s),

        if s < 0:
            start = mid + 1
        else:
            end = mid - 1

print(arr[idx1], arr[idx2])
