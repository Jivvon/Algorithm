import collections
from typing import List

from timer import timer

DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


# 좋아요 가장 많은 풀이
@timer
def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


# 내 풀이
@timer
def _solution(bridge_length: int, weight: int, truck_weights: List[int]) -> int:
    """
    들어갈 때 다리가 버틸 수 있어야 들어가도록
    남은게 비었으면 큐에 남은 마지막거의 시간 + length
    들어갈 때의 시간을 인덱스로 같이 넣자
    """
    running_q = [(0, truck_weights[0])]
    cur_time = 1
    i = 1

    while i < len(truck_weights):
        # 첫 차 도착했는지 확인
        if cur_time - running_q[0][0] >= bridge_length:
            running_q.pop(0)
        # 다음 차 출발할 수 있는지 확인
        if sum(map(lambda x: x[1], running_q)) + truck_weights[i] <= weight:
            running_q.append((cur_time, truck_weights[i]))
            i += 1
        cur_time += 1

    return running_q[-1][0] + bridge_length + 1


if __name__ == '__main__':
    solution(2, 10, [7, 4, 5, 6]) # 8
    solution(100, 100, [10]) # 101
    solution(100, 100, [10,10,10,10,10,10,10,10,10,10]) # 110
