"""
노가다 같아서 포기..
"""

import sys


# t = int(sys.stdin.readline().rstrip())


def rotate(arr, degree):
    """
    0,0 0,2 0,4 2,4 4,4 4,2 4,0 2,0 ~
    1,1 1,2 1,3 2,3 3,3 3,2 3,1 2,1 ~
    2,2
    :param arr:
    :param degree:
    :return:
    """
    d = (degree + 360) // 45 % 8
    n = len(arr)
    n2 = n // 2
    positions = [[] for _ in range(n2 + 1)]
    for i in range(n2):
        positions[i].extend([[i, j] for j in range(i, n - i, n2 - i)])
        l = positions[i][-1][1]
        positions[i].extend([[j, l] for j in range(n2, n - i, n2 - i)])
        tmp_arr = positions[i][1:len(positions[i]) - 1]
        tmp_arr.reverse()
        for tmp in tmp_arr:
            positions[i].append(tmp[::-1])
    positions[n2] = [n2, n2]
    return positions


# for _ in range(t):
n, d = map(int, sys.stdin.readline().rstrip().split())
arr = []
for __ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

for a in rotate(arr, 0):
    print(a)
