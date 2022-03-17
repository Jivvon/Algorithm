import sys


def rotate(arr, n, m, r):
    n2, m2 = n // 2, m // 2
    """
    y,x
    i,i -> m-i,i -> m-i,n-i -> i,n-i -> i,i
        m-i     n-i         m-i         n-i
    """
    for i in range(min(n2, m2)):
        dy = [k for k in range(i, n - i - 1)] + \
             [n - i - 1] * (m - 2 * i - 1) + \
             [k for k in range(n - i - 1, i, -1)] + \
             [i] * (m - 2 * i - 1)
        dx = [i] * (n - 2 * i - 1) + \
             [k for k in range(i, m - i - 1)] + \
             [m - i - 1] * (n - 2 * i - 1) + \
             [k for k in range(m - i - 1, i, -1)]
        prev = [arr[ny][nx] for nx, ny in zip(dx, dy)]
        l = len(prev)
        for j in range(l):
            arr[dy[j]][dx[j]] = prev[(j - r) % l]


def solution():
    n, m, r = map(int, sys.stdin.readline().rstrip().split())
    arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]  # arr[n][m], arr[y][x]
    rotate(arr, n, m, r)
    for a in arr:
        print(*a)


if __name__ == '__main__':
    solution()
