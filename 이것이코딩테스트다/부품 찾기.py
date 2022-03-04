from utils.timer import timer
from typing import List


# 내 풀이
@timer
def solution(n: int, sources: List[int], m: int, targets: List[int]):
    sources_asc = sorted(sources)
    targets_asc = sorted(targets)
    answers = []

    for idx_target, target in enumerate(targets_asc):
        start, end, mid = 0, n - 1, n // 2
        has_cur = "no"
        while True:
            if sources_asc[mid] == target:
                has_cur = "yes"
                break
            elif sources_asc[mid] < target:
                start = mid
            elif sources_asc[mid] > target:
                end = mid
            mid = start + (end - start) // 2
            if start == mid or end == mid:
                if sources_asc[start] == target or sources_asc[end] == target:
                    has_cur = "yes"
                break
        answers.append(has_cur)

    return " ".join(answers)


# Pythonic
@timer
def _solution(n: int, sources: List[int], m: int, targets: List[int]):
    return " ".join("yes" if target in sources else "no" for target in targets)


# 책 답안
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
    return None


@timer
def __solution(n: int, sources: List[int], m: int, targets: List[int]):
    sources_asc = sorted(sources)
    answers = ["no" if binary_search(sources_asc, target, 0, n - 1) is None else "yes" for target in targets]
    return " ".join(answers)


if __name__ == '__main__':
    __solution(5, [8, 3, 7, 9, 2], 3, [5, 7, 9])  # no yes yes
