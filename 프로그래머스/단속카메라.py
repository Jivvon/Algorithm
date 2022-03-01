from typing import List

from utils.timer import timer


@timer
def _solution(routes: List[List[int]]):
	routes.sort()
	_, cur = routes.pop(0)


@timer
def solution(routes: List[List[int]]):
	routes.sort(key=lambda x: (x[1], x[0]), reverse=True)
	answer = 0
	while routes:
		_, pos = routes.pop()
		for idx, route in enumerate(routes):
			if route[0] <= pos:
				routes.pop(idx)
		answer += 1
	return answer


if __name__ == '__main__':
	solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]])  # 2
	solution([[-30000, 1], [1, 5], [5, 6], [3, 100], [2, 3], [1, 2]])  # 3
	solution([[-100, 100], [50, 170], [150, 200], [-50, -10], [10, 20], [30, 40]])  # 4
