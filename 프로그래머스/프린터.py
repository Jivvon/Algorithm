from itertools import cycle
from typing import List


def solution(priorities: List[int], location: int) -> int:
    l = len(priorities)
    answer = 0
    cursor = 0
    while True:
        if max(priorities) == priorities[cursor]:
            answer += 1
            priorities[cursor] = 0
            if cursor == location:
                break
        cursor = (cursor + 1) % l
    return answer


def __solution(priorities: List[int], location: int) -> int:
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        v = queue.pop(0)
        if any(v[1] < q[1] for q in queue):
            queue.append(v)
        else:
            answer += 1
            if v[0] == location:
                return answer


def _solution(priorities: List[int], location: int) -> int:
    c = cycle(priorities)
    i = 0
    l = len(priorities)
    arr = [0] * len(priorities)
    while True:
        m = max(priorities)
        if next(c) == m:
            arr[i] = max(arr) + 1
            if i == location:
                return arr[i]
            priorities[i] = -1
        i = (i + 1) % l


if __name__ == '__main__':
    a = solution([2, 1, 3, 2], 2)
    print(a)  # == 1
    a = solution([1, 1, 9, 1, 1, 1], 0)
    print(a)  # == 5
    a = solution([9, 1], 1)
    print(a)  # == 2
    a = solution([3, 2, 5, 8, 4, 1, 5], 4)
    print(a)  # == 4
