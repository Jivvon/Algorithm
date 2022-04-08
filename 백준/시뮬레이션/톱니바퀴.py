"""
재귀로 구현하지 않는게 더 나을듯
처음에 양쪽으로 for i in range(idx+1, n) 이렇게 돌리면 될듯
"""
import sys
from collections import deque

gears = [deque(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(4)]
k = int(sys.stdin.readline().rstrip())


def rotate_gear(gear_num, direction, prev_gear_num=None):
    cur_left, cur_right = gears[gear_num][6], gears[gear_num][2]
    gears[gear_num].rotate(direction)
    if gear_num == 0:
        if prev_gear_num is None and gears[gear_num + 1][6] != cur_right:
            rotate_gear(gear_num + 1, -1 * direction, gear_num)
    elif gear_num == 3:
        if prev_gear_num is None and gears[gear_num - 1][2] != cur_left:
            rotate_gear(gear_num - 1, -1 * direction, gear_num)
    else:
        if prev_gear_num is None:
            if gears[gear_num + 1][6] != cur_right:
                rotate_gear(gear_num + 1, -1 * direction, gear_num)
            if gears[gear_num - 1][2] != cur_left:
                rotate_gear(gear_num - 1, -1 * direction, gear_num)
        else:
            if gear_num - prev_gear_num == 1 and gears[gear_num + 1][6] != cur_right:
                rotate_gear(gear_num + 1, -1 * direction, gear_num)
            elif gear_num - prev_gear_num == -1 and gears[gear_num - 1][2] != cur_left:
                rotate_gear(gear_num - 1, -1 * direction, gear_num)


for _ in range(k):
    gear_num, direction = map(int, sys.stdin.readline().rstrip().split())
    gear_num -= 1
    rotate_gear(gear_num, direction)

answer = 0
for idx, gear in enumerate(gears):
    north_num = gear[0]
    if north_num == 1:
        answer += 1 << idx

print(answer)
