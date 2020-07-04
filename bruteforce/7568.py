import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()

N = int(input())
compared = [[0 for _ in range(N)] for __ in range(N)]
people = [list(map(int, input().split())) for _ in range(N)]

ret = [1 for i in range(N)]
for i in range(N):
    for j in range(i+1, N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            ret[i] += 1
        elif people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            ret[j] += 1

print(' '.join(map(str, ret)))
