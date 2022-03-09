import sys
import bisect

input = sys.stdin.readline

n, m = map(int, input().split())
points = list(map(int, input().split()))
points.sort()

for _ in range(m):
    start, end = map(int, input().split())
    a = bisect.bisect_left(points, start)
    b = bisect.bisect_right(points, end)
    print(b - a)
