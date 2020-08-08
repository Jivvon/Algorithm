import sys
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]
arr = sorted(arr, key=lambda x:(x[1],x[0]))
ans = time = 0

for s, e in arr:
    if s >= time:
        ans += 1
        time = e

print(ans)
