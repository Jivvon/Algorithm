from typing import List

from utils.timer import timer

INF = int(1e9)


@timer
def solution(n: int, vertex: List[List[int]]):
		from collections import defaultdict, deque

		def bfs(graph, start, distances):
				q = deque([start])
				visited = {start}

				while q:
						current = q.popleft()
						for neighbor in graph[current]:
								if neighbor not in visited:
										visited.add(neighbor)
										q.append(neighbor)
										distances[neighbor] = distances[current] + 1

		# 그래프 만들기
		graph = defaultdict(list)
		for e in vertex:
				graph[e[0]].append(e[1])
				graph[e[1]].append(e[0])
		distance = [0] * (n + 1)

		bfs(graph, 1, distance)

		answer = len(list(filter(lambda x: x == max(distance[1:]), distance[1:])))
		return answer


# 내 풀이
@timer
def _solution(n: int, vertex: List[List[int]]):
		from collections import deque

		distance = [INF] * (n + 1)
		graph = {k: [] for k in range(1, n + 1)}
		for v in vertex:
				graph[v[0]].append(v[1])
				graph[v[1]].append(v[0])

		q = deque()  # 도착 vertex, cost
		q.append((1, 0))
		while q:
				to_vertex, cost = q.popleft()
				if cost < distance[to_vertex]:
						distance[to_vertex] = cost
						q.extend([(i, cost + 1) for i in graph[to_vertex]])

		distance = list(map(lambda x: -1 if x == INF else x, distance))
		answer = len(list(filter(lambda x: x == max(distance[1:]), distance[1:])))
		return answer


if __name__ == '__main__':
		n = 6
		vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
		solution(n, vertex)  # 3
		n = 2
		vertex = [[1, 2]]
		solution(n, vertex)  # 1
		n = 3
		vertex = [[1, 2], [3, 1]]
		solution(n, vertex)  # 2
		n = 4
		vertex = [[1, 2], [3, 1], [3, 2], [2, 4], [3, 4]]
		solution(n, vertex)  # 1
