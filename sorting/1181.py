import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
arr = [input() for _ in range(N)]
arr = sorted(set(arr), key=lambda x:(len(x), x))
for _ in arr:
    print(_)
