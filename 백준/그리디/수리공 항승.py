import sys

n, l = map(int, sys.stdin.readline().rstrip().split())
positions = list(sorted(map(int, sys.stdin.readline().rstrip().split())))
prev = 0
count = 0

for pos in positions:
    if pos > prev:
        prev = pos + l - 1
        count += 1

print(count)
