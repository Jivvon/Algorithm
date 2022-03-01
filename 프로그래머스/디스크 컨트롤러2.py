from typing import List

from utils.timer import timer


@timer
def solution(jobs: List[List[int]]):
    # 가장 짧은 것부터 하자
    from collections import deque
    import heapq

    tasks = deque(sorted([[x[1], x[0]] for x in jobs], key=lambda x: (x[1], x[0])))
    q = [tasks.popleft()]
    heapq.heapify(q)

    cur_time, answer = 0, 0
    while q:
        duration, req_time = heapq.heappop(q)
        if cur_time < req_time:
            cur_time = req_time
        cur_time += duration
        answer += cur_time - req_time

        while tasks and tasks[0][1] <= cur_time:
            heapq.heappush(q, tasks.popleft())
        if tasks and len(q) == 0:
            heapq.heappush(q, tasks.popleft())

    answer = answer // len(jobs)
    return answer


if __name__ == '__main__':
    solution([[0, 3], [1, 9], [2, 6]])  # 9
    """
    1. 시간 순 2. 짧은 순
    heap에서 짧은 순 힙 할거니까 순서 바꾸고
    
    가장 먼저 실행되는 애 중에 가장 짧은애 넣고
    시간 계산하면서 현재 시간 now 업데이트하고
    뒤로 가면 그 앞에서 이미 요청 들어온애들 전부 힙에 넣는거지
    개굿
    """
    solution([[0, 1], [100, 2], [101, 20]])  # 8
