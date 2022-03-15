import sys


def fill_border(arr, n, start, x, y):
    """
    3 => x,y = 1,2
    dx [1 1 2 3 3 3 2 1]
    dy [2 3 3 3 2 1 1 1]
    """
    dx = [x] * (n - 1) + \
         [i for i in range(x + 1, n + x)] + \
         [n + x - 1] * (n - 1) + \
         [i for i in range(n + x - 2, x - 1, -1)]
    dy = [i for i in range(y, n + y - 2)] + \
         [n + y - 2] * (n - 1) + \
         [i for i in range(n + y - 2, y - 2, -1)] + \
         [y - 1] * (n - 1)
    for i, (x, y) in enumerate(zip(dx, dy)):
        arr[x][y] = start + i


def solution():
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    arr = [[0] * n for _ in range(n)]

    n2 = n // 2
    arr[n2][n2] = 1
    for i in range(n2):
        fill_border(arr, n - 2 * i, (n - 2 * (i + 1)) ** 2 + 1, i, i + 1)

    for idx, ar in enumerate(arr):
        if m in ar:
            x = idx + 1
            y = ar.index(m) + 1
        print(" ".join(map(str, ar)))

    print(x, y)


if __name__ == '__main__':
    solution()
