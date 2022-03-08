"""
범위: 1 ~ 최악의 경우 걸리는 시간
기준: mid 시간 동안 가능한 사람 수
    m보다 크면 여유로운거니까 end = mid - 1
    m보다 작으면 바빠서 다 못한거니까 start = mid + 1
"""
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
times = sorted(int(sys.stdin.readline().rstrip()) for _ in range(n))
start, end = 1, times[0] * m
answer = 0

while start <= end:
    mid = (start + end) // 2
    can_people = sum(list(map(lambda x: mid // x, times)))
    if can_people >= m:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
