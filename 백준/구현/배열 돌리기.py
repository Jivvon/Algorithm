import sys


def rotate(arr, n, d):
    n2 = n // 2
    step = (d % 360) // 45
    if step == 0:
        return
    for i in range(n2):
        dx = [i, n2, n2 * 2 - i, n2 * 2 - i, n2 * 2 - i, n2, i, i]
        dy = [i, i, i, n2, n2 * 2 - i, n2 * 2 - i, n2 * 2 - i, n2]
        prev = [arr[dy[j]][dx[j]] for j in range(8)]
        for j in range(8):
            arr[dy[(j + step) % 8]][dx[(j + step) % 8]] = prev[j]


def solution():
    n, d = map(int, sys.stdin.readline().rstrip().split())
    arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    rotate(arr, n, d)
    for a in arr:
        print(*a)


if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        solution()

"""
1
5 180
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
"""
