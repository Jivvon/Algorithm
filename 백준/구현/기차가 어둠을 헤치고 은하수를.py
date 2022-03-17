from collections import deque
import sys


def do(trains: list, comm: list):
    if comm[0] == 1:
        trains[comm[1] - 1][comm[2] - 1] = 1
    elif comm[0] == 2:
        trains[comm[1] - 1][comm[2] - 1] = 0
    elif comm[0] == 3:
        trains[comm[1] - 1].rotate(1)
        trains[comm[1] - 1][0] = 0
    elif comm[0] == 4:
        trains[comm[1] - 1].rotate(-1)
        trains[comm[1] - 1][-1] = 0


def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    trains = [deque([0] * 20) for _ in range(n)]
    for _ in range(m):
        comm = list(map(int, sys.stdin.readline().rstrip().split()))
        do(trains, comm)
    answer = len(set(map(str, trains)))
    print(answer)


if __name__ == '__main__':
    solution()
