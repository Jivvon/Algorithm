import sys

N = int(input())
arr = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))

cur, count = 0, 0
for i in arr:
    if cur <= i[0]:
        cur = i[1]
        count += 1

print(count)
