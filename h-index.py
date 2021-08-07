from typing import List


def solution(citations: List[int]):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


if __name__ == '__main__':
    print(solution([3, 0, 6, 1, 5]))
    print(solution([88, 89]))
    print(solution([0, 0, 0, 0, 1]))
    # assert solution([3, 0, 6, 1, 5]) == 3
