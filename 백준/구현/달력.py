import sys

n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

days = [0] * 366

for s, e in arr:
    for i in range(s, e + 1):
        days[i] += 1

answer = 0
w, h = 0, 0
for i in range(1, 366):
    if days[i] > 0:
        w += 1
        h = max(h, days[i])
    elif w > 0 and h > 0:
        answer += w * h
        w, h = 0, 0

answer += w * h
print(answer)
