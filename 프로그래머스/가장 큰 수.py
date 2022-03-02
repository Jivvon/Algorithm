from typing import List

from utils.timer import timer


@timer
def solution(numbers: List[int]):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x: x * 3, reverse=True)
    return ''.join(numbers)


if __name__ == '__main__':
    solution([6, 10, 2])  # 6210
    solution([3, 30, 34, 5, 9])  # 9534330
