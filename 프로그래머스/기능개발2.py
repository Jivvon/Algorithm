from typing import List

from utils.timer import timer


@timer
def solution(progresses: List[int], speeds: List[int]):
    from math import ceil

    q = [[ceil((100 - progresses[0]) / speeds[0]), 1]]  # [[duration, count], [..]]
    for progress, speed in zip(progresses[1:], speeds[1:]):
        duration = ceil((100 - progress) / speed)
        if q[-1][0] < duration:
            q.append([duration, 1])
        else:
            q[-1][1] += 1

    answer = [i[1] for i in q]
    return answer

    return answers


if __name__ == '__main__':
    solution([93, 30, 55], [1, 30, 5])  # 2 1
    solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])  # 1 3 2
    # solution([4, 4, 4], [2, 2, 2])  # 3
