import sys
from typing import List

from utils.timer import timer


def DFS(arr, x, y, N, M):
    if x < 0 or x >= N or y < 0 or y >= M:
        return 0
    if arr[x][y] == 0:
        arr[x][y] = 1
        DFS(arr, x - 1, y, N, M)
        DFS(arr, x + 1, y, N, M)
        DFS(arr, x, y - 1, N, M)
        DFS(arr, x, y + 1, N, M)
        return 1
    return 0


@timer
def solution(arr: List[List[int]], N, M):
    answer = 0
    for x in range(N):
        for y in range(M):
            answer += DFS(arr, x, y, N, M)

    print(answer)


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    arr = [0] * N
    for i in range(N):
        arr[i] = list(map(int, list(sys.stdin.readline())[:-1]))
    solution(arr, N, M)  # 3

"""
4 5
00110
00011
11111
00000
"""
