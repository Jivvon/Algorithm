import sys
from collections import defaultdict


# 2차원 union-find
def _find_parent(_parent, _x, _y):
    if _parent[_y][_x] != (_x, _y):
        nx, ny = _parent[_y][_x]
        _parent[_y][_x] = _find_parent(_parent, nx, ny)
    return _parent[_y][_x]


def _union(_parent, x1, y1, x2, y2):
    _a = _find_parent(_parent, x1, y1)
    _b = _find_parent(_parent, x2, y2)
    if _a < _b:
        _parent[y2][x2] = _a
    else:
        _parent[y1][x1] = _b
    return _parent


def near_union(_arr, _parent, _x, _y, _l, _r):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    _is_union = False

    for i in range(4):
        nx = _x + dx[i]
        ny = _y + dy[i]
        if (0 <= nx < n and 0 <= ny < n) \
                and _l <= abs(_arr[_y][_x] - _arr[ny][nx]) <= _r:
            _union(_parent, _x, _y, nx, ny)
            _is_union = True
    return _is_union


n, l, r = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
count = 0

while True:
    parent = [[(i, j) for i in range(n)] for j in range(n)]  # x,y
    is_union = False
    for i in range(n):
        for j in range(n):
            is_union = near_union(arr, parent, j, i, l, r) or is_union

    if not is_union:
        print(count)
        break

    group_sum = defaultdict(int)
    group_pos = defaultdict(list)
    for i in range(n):
        for j in range(n):
            p = _find_parent(parent, j, i)
            group_sum[p] += arr[i][j]
            group_pos[p].append((j, i))

    for k, v in group_pos.items():
        num = group_sum[k] // len(v)
        for x, y in v:
            arr[x][y] = num
    count += 1
