import sys
from typing import List, Tuple

input = sys.stdin.readline
INF = int(1e9)


def get_smallest_node(distance: List[int], visited: List[bool]):
		"""
		방문하지 않은 노드 중에서, 최단 거리가 가장 짧은 노드의 번호를 반환
		"""
		min_value = INF
		index = 0
		for i in range(1, n + 1):
				if distance[i] < min_value and not visited[i]:
						min_value = distance[i]
						index = i
		return index


def dijkstra(graph: List[List[Tuple[int, int]]], start: int, distance: List[int], visited: List[bool]):
		# 시작 노드 초기화
		distance[start] = 0
		visited[start] = True
		for j in graph[start]:
				distance[j[0]] = j[1]  # 시작 노드에서 연결된 노드로 가는 비용

		# 시작 노드를 제외한 n-1 개의 노드에 대해 반복
		for i in range(n - 1):
				cur_minimum = get_smallest_node(distance, visited)
				visited[cur_minimum] = True
				# 현재 노드와 연결된 다른 노드들 확인
				for j in graph[cur_minimum]:
						cost = distance[cur_minimum] + j[1]
						# 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
						if cost < distance[j[0]]:
								distance[j[0]] = cost  # 갱신


if __name__ == '__main__':
		n, m = map(int, input().split())  # 노드의 개수, 간선의 개수
		start = int(input())  # 시작 지점

		graph = [[] for _ in range(n + 1)]
		visited = [False] * (n + 1)
		distance = [INF] * (n + 1)

		# 그래프 입력
		for _ in range(m):
				a, b, c = map(int, input().split())  # a에서 b로 가는 비용이 c
				graph[a].append((b, c))

		dijkstra(graph, start, distance, visited)

		# 모든 노드로 가기 위한 최단 거리를 출력
		ret = list(map(lambda x: -1 if x == INF else x, distance[1:]))
		print(ret)
