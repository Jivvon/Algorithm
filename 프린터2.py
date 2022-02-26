from typing import List

from utils.timer import timer


@timer
def solution(priorities: List[int], location: int):
    from collections import deque

    queue = deque(enumerate(priorities))  # [idx, priority]
    answers = []

    while queue:
        cur = queue.popleft()
        if len(queue) == 0 or cur[1] >= max(queue, key=lambda x: x[1])[1]:
            answers.append(cur[0])
        else:
            queue.append(cur)

    answer = answers.index(location) + 1
    return answer


if __name__ == '__main__':
    solution([2, 1, 3, 2], 2)
    solution([1, 1, 9, 1, 1, 1], 0)
    solution([9, 1], 1)
    solution([3, 2, 5, 8, 4, 1, 5], 4)
