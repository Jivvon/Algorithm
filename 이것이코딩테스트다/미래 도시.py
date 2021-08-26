"""
플로이드 워셜 알고리즘
"""
from typing import List

from utils.timer import timer

INF = int(1e9)


@timer
def solution(n, m, arr: List[List[int]], x, k):
		"""
		1번에서 출발하여 k번을 방문한 뒤 x번으로 가는 것이 목표다
		최소 이동 시간은?
		모든 간선의 비용은 1

		:param n: 노드 개수
		:param m: 간선의 수
		:param arr: 연결 정보
		:param x: 도착지
		:param k: 경유지
		:return: 최소 비용
		"""
		graph = [[INF] * (n + 1) for _ in range(n + 1)]
		for i in range(1, n + 1):
				graph[i][i] = 0

		for e in arr:
				graph[e[0]][e[1]] = graph[e[1]][e[0]] = 1

		for node in range(1, n + 1):
				for a in range(1, n + 1):
						for b in range(1, n + 1):
								graph[a][b] = min(graph[a][b], graph[a][node] + graph[node][b])

		answer = graph[1][k] + graph[k][x]

		return answer if answer < INF else -1


if __name__ == '__main__':
		arr = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4], [3, 5], [4, 5]]
		solution(5, 7, arr, 4, 5)
		arr = [[1, 3], [2, 4]]
		solution(4, 2, arr, 3, 4)
