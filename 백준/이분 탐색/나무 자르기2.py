import math
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
trees = sorted(list(map(int, sys.stdin.readline().rstrip().split())))


# 나무 길이 기준으로 이진 탐색

def gt_m(height):
    total = 0
    for x in trees:
        if x > height:
            total += x - height
    return total
    # return sum(list(map(lambda x: x - height if x > height else False, trees))) >= m


l, r, answer = 0, int(2e9), 0
while l <= r:
    mid = (l + r) // 2
    if gt_m(mid):
        answer = mid
        l = mid + 1
    else:
        r = mid - 1

print(answer)
