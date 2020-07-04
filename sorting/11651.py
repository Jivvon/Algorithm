import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = sorted(arr, key=lambda x: (x[1],x[0]))
for _ in arr:
    print(' '.join(map(str,_)))
