import sys
import math

N, M, K = map(int, sys.stdin.readline().split())

an, bn = divmod(N, 2)
teams = min(an, M)

if an <= M:
    remain = M - an + bn
elif an > M:
    remain = 2 * (an - M) + bn

K -= remain
if K > 0:
    teams -= math.ceil(K / 3)

print(teams)
