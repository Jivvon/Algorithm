import sys
from utils.timer import timer


@timer
def solution(n, m, arr, moves):
    clouds = [(n - 2, 0), (n - 1, 0), (n - 2, 1), (n - 1, 1)]  # row, col = y,x
    for d, s in moves:
        clouds = move(clouds, n, d, s)
        rain(arr, clouds)
        cheet(arr, n, clouds)
        clouds = select_clouds(arr, n, clouds)
    return sum(map(sum, arr))


def move(clouds, n, d, s):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    nx, ny = dx[d - 1] * s, dy[d - 1] * s

    new_clouds = []
    for cloud in clouds:
        _y = (cloud[0] + ny) % n
        _x = (cloud[1] + nx) % n
        new_clouds.append((_y, _x))
    return new_clouds


def rain(arr, clouds):
    for y, x in clouds:
        arr[y][x] += 1


def cheet(arr, n, clouds):
    dx = [-1, 1, 1, -1]
    dy = [-1, -1, 1, 1]
    for cloud_y, cloud_x in clouds:
        for i in range(4):
            nx = dx[i] + cloud_x
            ny = dy[i] + cloud_y
            if (0 <= nx < n and 0 <= ny < n) and \
                    arr[ny][nx] > 0:
                arr[cloud_y][cloud_x] += 1


def select_clouds(arr, n, clouds):
    new_clouds = []
    for row in range(n):
        for col in range(n):
            if arr[row][col] >= 2 and (row, col) not in clouds:
                new_clouds.append((row, col))
                arr[row][col] -= 2
    return new_clouds


if __name__ == '__main__':
    # n, m = map(int, sys.stdin.readline().rstrip().split())
    # arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    # moves = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]
    # answer = solution(n, m, arr, moves)
    # print(answer)

    ret = solution(5, 4,
                   [[0, 0, 1, 0, 2],
                    [2, 3, 2, 1, 0],
                    [4, 3, 2, 9, 0],
                    [1, 0, 2, 9, 0],
                    [8, 8, 2, 1, 0]],
                   [[1, 3],
                    [3, 4],
                    [8, 1],
                    [4, 8]]
                   )
    print("answer = ", ret, ret == 77)
    ret = solution(5, 8,
                   [[0, 0, 1, 0, 2],
                    [2, 3, 2, 1, 0],
                    [0, 0, 2, 0, 0],
                    [1, 0, 2, 0, 0],
                    [0, 0, 2, 1, 0]],
                   [[1, 9],
                    [2, 8],
                    [3, 7],
                    [4, 6],
                    [5, 5],
                    [6, 4],
                    [7, 3],
                    [8, 2]])
    print("answer = ", ret, ret == 41)
    ret = solution(5, 8,
                   [[100, 100, 100, 100, 100],
                    [100, 100, 100, 100, 100],
                    [100, 100, 100, 100, 100],
                    [100, 100, 100, 100, 100],
                    [100, 100, 100, 100, 100]],
                   [[8, 1],
                    [7, 1],
                    [6, 1],
                    [5, 1],
                    [4, 1],
                    [3, 1],
                    [2, 1],
                    [1, 1]])
    print("answer = ", ret, ret == 2657)
