from typing import List

from utils.timer import timer


@timer
def solution(n: int, costs: List[List[int]]):
	if n == 1:
		return 0

	costs.sort(key=lambda x: x[2])  # 비용순으로 정렬

	start = costs[0]
	routes = set([start[0], start[1]])
	answer = start[2]

	while len(routes) != n:
		for idx, (i, j, cost) in enumerate(costs[1:]):
			if i == -1 or j == -1:  # 이미 처리했던 루트라면 스킵
				continue
			if i in routes and j in routes:  # 둘 다 포함되어 있으면 스킵
				continue
			if i in routes or j in routes:  # 둘 중 하나만 포함되어 있으면 연결
				routes.update([i, j])
				answer += cost
				costs[idx + 1] = [-1, -1, -1]
				break

	return answer


if __name__ == '__main__':
	solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])  # 4
	solution(1, [])  # 0
	solution(2, [[0, 1, 10]])  # 10
	solution(3, [[0, 1, 10], [1, 2, 11]])  # 21
	solution(7, [
		[0, 1, 1],
		[0, 2, 1],
		[1, 2, 2],
		[1, 3, 3],
		[1, 5, 3],
		[2, 3, 1],
		[2, 4, 1],
		[2, 6, 4],
		[3, 5, 1],
		[3, 6, 1],
		[4, 6, 2],
	])  # 6
