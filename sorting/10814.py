import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
arr = [list(input().split()) for _ in range(N)]
arr = sorted(arr, key=lambda x: (int(x[0])))

for i in arr:
    print(*i)
