from typing import List
from collections import deque


# 위상 정렬
def topology_sort(graph: List[List[int]], indegree: List[int]):
		result = []
		q = deque()

		# 1. 진입 차수가 0인 노드 큐에 삽입
		for idx, val in enumerate(indegree):
				if val == 0:
						q.append(idx)

		# 큐가 빌 때까지
		# 진입 차수가 0인 노드를 삽입하고 간선을 삭제한다 (도착지의 진입 차수 -1)
		while q:
				now = q.popleft()
				result.append(now)
				# 해당 원소와 연결된 노드들의 진입 차수에서 1 빼기
				for i in graph[now]:
						indegree[i] -= 1
						# 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
						if indegree[i] == 0:
								q.append(i)

		return result[1:]


if __name__ == '__main__':
		v, e = 7, 8  # vertex, edge
		arr = [
				[1, 2],
				[1, 5],
				[2, 3],
				[2, 6],
				[3, 4],
				[4, 7],
				[5, 6],
				[6, 4]
		]

		# 1. 모든 노드에 대한 진입차수는 0으로 초기화
		indegree = [0] * (v + 1)
		# 2. 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
		graph = [[] for i in range(v + 1)]

		# a에서 b로 이동 가능
		for a, b in arr:
				graph[a].append(b)
				indegree[b] += 1  # 진입차수 + 1

		ret = topology_sort(graph, indegree)
		print(ret)
