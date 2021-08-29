from typing import List

from utils.timer import timer


@timer
def solution(n: int, arr: List[List[int]]):
		"""

		:param n: 노드 개수
		:param arr: 노드와 간선 정보
		:return:
		"""
		from collections import deque

		answers = [0] * (n + 1)
		graph = [[]] * (n + 1)
		costs = [0] * (n + 1)
		indegrees = [0] * (n + 1)
		q = deque()

		for idx, ar in enumerate(arr):
				costs[idx + 1] = ar[0]
				graph[idx + 1] = ar[1:-1]
				indegrees[idx + 1] = len(ar[1:-1])
				if indegrees[idx + 1] == 0:
						q.append(idx + 1)

		while q:
				cur = q.popleft()
				answers[cur] = max([answers[i] for i in graph[cur]] + [0]) + costs[cur]
				for idx, j in enumerate(graph):
						if cur in j:
								indegrees[idx] -= 1
								if indegrees[idx] == 0:
										q.append(idx)

		return answers[1:]


if __name__ == '__main__':
		n = 5
		arr = [
				[10, -1],
				[10, 1, -1],
				[4, 1, -1],
				[4, 3, 1, -1],
				[3, 3, -1]
		]
		solution(n, arr)
