import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    sys.stdin.readline()
    l = list(sorted(map(int, sys.stdin.readline().rstrip().split())))
    print(l[0], l[-1])

