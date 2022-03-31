import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def rotate(pos, d, d_rotate):
    if d_rotate == "L":
        d = (d - 1) % 4
    elif d_rotate == "D":
        d = (d + 1) % 4
    return [pos[0] + dx[d], pos[1] + dy[d]], d


def move(n, queue: deque, apples, d, d_rotate=None):
    """

    :param n:
    :param apples:
    :param queue:
    :param d: 좌 상 우 하 = 0 1 2 3
    :param d_rotate: L R
    :return:
    """

    last = queue[-1]
    if d_rotate:
        next_pos, d = rotate(last, d, d_rotate)
    else:
        next_pos = [last[0] + dx[d], last[1] + dy[d]]

    if not (0 <= next_pos[0] < n and 0 <= next_pos[1] < n) \
            or next_pos in queue:
        return False, d

    queue.append(next_pos)
    if next_pos in apples:
        apples.remove(next_pos)
    else:
        queue.popleft()
    return True, d


def solution(n, apples, rotates):
    cur_d = 2  # 오른쪽
    cur = 0
    ret = True
    snake = deque([[0, 0]])
    while ret:
        cur += 1
        if rotates and cur == rotates[0][0]:
            rotate_info = rotates.popleft()
            ret, cur_d = move(n, snake, apples, cur_d, d_rotate=rotate_info[1])
        else:
            ret, cur_d = move(n, snake, apples, cur_d)
    return cur


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    k = int(sys.stdin.readline().rstrip())
    apples = []  # x, y
    for _ in range(k):
        tmp = list(map(int, sys.stdin.readline().rstrip().split()))
        apples.append([tmp[1] - 1, tmp[0] - 1])
    l = int(sys.stdin.readline().rstrip())
    rotates = deque()  # [0]초 째에 [1] 방향으로 회전
    for _ in range(l):
        tmp = sys.stdin.readline().rstrip().split()
        rotates.append([int(tmp[0]) + 1, tmp[1]])
    answer = solution(n, apples, rotates)
    print(answer)
