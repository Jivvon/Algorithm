from typing import List


def solution(array: List[int], commands: List[List[int]]):
    answer = []

    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i-1:j])[k-1])

    return answer


if __name__ == '__main__':
    assert solution([1, 5, 2, 6, 3, 7, 4]	,
             [[2, 5, 3], [4, 4, 1], [1, 7, 3]]) == [5, 6, 3]
