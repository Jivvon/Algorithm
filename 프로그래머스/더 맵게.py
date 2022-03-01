from typing import List

from utils.timer import timer


@timer
def solution(scoville: List[int], k: int):
		import heapq
		heapq.heapify(scoville)
		answer = 0
		while True:
				min1 = heapq.heappop(scoville)
				if min1 >= k:
						return answer
				if not scoville:
						break
				min2 = heapq.heappop(scoville)
				heapq.heappush(scoville, min1 + (2 * min2))
				answer += 1
		return -1


if __name__ == '__main__':
		solution([1, 2, 3, 9, 10, 12], 7)  # 2
		solution([1, 2, 3], 11)  # 2
