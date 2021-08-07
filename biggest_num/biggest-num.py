import itertools
from typing import List


def solution(numbers: List[int]):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x:x*3, reverse=True)
    return str(int(''.join(numbers)))


if __name__ == '__main__':
    print(solution([6, 10, 2]))
    print(solution(	[3, 30, 34, 5, 9]))
    print(solution([0, 0, 0, 0]))
    # a = [6, 10, 2]
    # a = ''.join(map(str, a))
    # print(a)
    # a = sorted("5123")[::-1]
    # print(a)
