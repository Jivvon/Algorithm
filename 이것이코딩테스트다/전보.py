from typing import List

from utils.timer import timer

INF = int(1e9)


# 다익스트라
@timer
def solution(n, m, arr: List[List[int]], c):
		"""

		:param n: 노드 개수
		:param m: 간선 개수
		:param arr: [0]에서 [1]로 가는데 걸리는 비용[2]의 리스트
		:param c: 출발지
		:return: 출발지에서 갈 수 있는 노드의 수와 모두 갔을 때 걸리는 시간 (최대값)
		"""
		import heapq
		distance = [INF] * (n + 1)
		q = []
		# graph = [] * (n + 1)  # value에서 출발하여 value[0]에 도착하는데 걸리는 비용은 value[1]이다
		# for e in arr:
		# 		graph[e[0]].append((e[1], e[2]))

		distance[c] = 0
		heapq.heappush(q, (0, c))
		while q:
				dist, node = heapq.heappop(q)
				if distance[node] < dist:
						continue
				for e in list(filter(lambda x: x[0] == node, arr)):
						dst = e[1]
						cost = e[2] + dist
						if cost < distance[dst]:
								distance[dst] = cost
								heapq.heappush(q, (cost, dst))
		reachable_nodes = list(filter(lambda x: x, distance[1:]))
		return len(reachable_nodes), max(reachable_nodes)


# 시간 초과
# 플로이드 워샬
@timer
def _solution(n, m, arr: List[List[int]], c):
		"""

		:param n: 노드 개수
		:param m: 간선 개수
		:param arr: [0]에서 [1]로 가는데 걸리는 비용[2]의 리스트
		:param c: 출발지
		:return: 출발지에서 갈 수 있는 노드의 수와 모두 갔을 때 걸리는 시간 (최대값)
		"""
		graph = [[INF] * (n + 1) for _ in range(n + 1)]
		for i in range(1, n + 1):
				graph[i][i] = 0

		for e in arr:
				graph[e[0]][e[1]] = e[2]

		"""플로이드 워샬"""

		for node in range(1, n + 1):
				for a in range(1, n + 1):
						for b in range(1, n + 1):
								graph[a][b] = min(graph[a][b], graph[a][node] + graph[node][b])

		reachable_nodes = list(filter(lambda x: x != INF and x != 0, graph[c][1:]))
		return len(reachable_nodes), max(reachable_nodes)


if __name__ == '__main__':
		arr = [[1, 2, 4], [1, 3, 2]]
		solution(3, 2, arr, 1)  # 2 4
