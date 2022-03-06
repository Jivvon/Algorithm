import sys
import bisect

test_case = int(input())

for _ in range(test_case):
    N, M = map(int, input().split())
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    B = list(map(int, sys.stdin.readline().rstrip().split()))
    answer = 0

    B.sort()
    for a in A:
        answer += bisect.bisect_left(B, a)
    print(answer)
