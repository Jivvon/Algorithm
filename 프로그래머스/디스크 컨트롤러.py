from typing import List

from utils.timer import timer


@timer
def solution(jobs: List[List[int]]):
		import heapq
		from collections import deque

		tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
		q = []
		heapq.heappush(q, tasks.popleft())
		current_time, total_response_time = 0, 0
		while len(q) > 0:
				dur, arr = heapq.heappop(q)
				current_time = max(current_time + dur, arr + dur)
				total_response_time += current_time - arr
				while len(tasks) > 0 and tasks[0][1] <= current_time:
						heapq.heappush(q, tasks.popleft())
				if len(tasks) > 0 and len(q) == 0:
						heapq.heappush(q, tasks.popleft())
		return total_response_time // len(jobs)


# 내 풀이
@timer
def _solution(jobs: List[List[int]]):
		"""
		cur_time 까지 들어온 요청 중 작은 것부터 처리
		"""
		cur_time = 0
		l = len(jobs)
		total = 0
		cur_jobs = []

		import heapq
		heapq.heapify(jobs)
		while jobs or cur_jobs:
				while jobs:
						job = heapq.heappop(jobs)
						if job[0] <= cur_time:
								heapq.heappush(cur_jobs, job[::-1])
						else:
								heapq.heappush(jobs, job)
								break
				if cur_jobs:
						duration, start_time = heapq.heappop(cur_jobs)
						cur_time += duration
						total += cur_time - start_time
				else:
						cur_time += 1
		answer = total // l
		return answer


if __name__ == '__main__':
		solution([[0, 3], [1, 9], [2, 6]])  # 9
		solution([[0, 1], [100, 2], [101, 20]])  # 8
