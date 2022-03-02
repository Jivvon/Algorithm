from typing import List

from utils.timer import timer

answer = 0


def dfs(numbers, idx, total, target):
    global answer
    if len(numbers) == idx:
        if total == target:
            answer += 1
        return 0
    dfs(numbers, idx + 1, total + numbers[idx], target)
    dfs(numbers, idx + 1, total - numbers[idx], target)


@timer
def solution(numbers: List[int], target: int):
    global answer
    dfs(numbers, 0, 0, target)
    return answer


# Pythonic한 풀이
@timer
def _solution(numbers: List[int], target: int):
    from itertools import product
    l = [(x, -x) for x in numbers]
    answers = list(map(sum, product(*l)))
    return answers.count(target)


if __name__ == '__main__':
    _solution([1, 1, 1, 1, 1], 3)
    _solution([4, 1, 2, 1], 4)
