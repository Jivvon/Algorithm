import math
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
trees = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

l, r = 0, n - 1
total = 0

while l <= r:
    mid = (l + r) // 2
    total = sum(list(map(lambda x: x - trees[mid], trees[mid + 1:])))
    if total == m:
        answer = trees[mid]
        break
    elif total > m:
        l = mid + 1
    elif total < m:
        r = mid - 1

if mid == r:
    mid += 1

total = sum(list(map(lambda x: x - trees[mid], trees[mid + 1:])))
cut_trees = (n - 1) - (mid - 1)
answer = trees[mid] - math.ceil((m - total) / cut_trees)

print(answer)
