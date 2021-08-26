import sys
import heapq

from typing import List, Tuple

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(graph: List[List[Tuple[int, int]]], start: int, distance: List[int]):
		q = []
		# 시작 노드 초기화
		distance[start] = 0
		heapq.heappush(q, (0, start))  # 시작 노드로 가기 위한 최단 경로는 0

		while q:
				dist, cur_minimum = heapq.heappop(q)
				# 현재 노드가 이미 처리된 적이 있다면 무시
				if distance[cur_minimum] < dist:
						continue
				# 현재 노드와 연결된 다른 노드들 확인
				for i in graph[cur_minimum]:
						cost = dist + i[1]
						# 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
						if cost < distance[i[0]]:
								distance[i[0]] = cost  # 갱신
								heapq.heappush(q, (cost, i[0]))


if __name__ == '__main__':
		n, m = map(int, input().split())  # 노드의 개수, 간선의 개수
		start = int(input())  # 시작 지점

		graph = [[] for _ in range(n + 1)]
		distance = [INF] * (n + 1)

		# 그래프 입력
		for _ in range(m):
				a, b, c = map(int, input().split())  # a에서 b로 가는 비용이 c
				graph[a].append((b, c))

		dijkstra(graph, start, distance)

		# 모든 노드로 가기 위한 최단 거리를 출력
		ret = list(map(lambda x: -1 if x == INF else x, distance[1:]))
		print(ret)
