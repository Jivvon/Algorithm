INF = int(1e9)

if __name__ == '__main__':
		# 노드 개수, 간선 개수
		n, m = 4, 7
		input_graph = [
				"1 2 4",
				"1 4 6",
				"2 1 3",
				"2 3 7",
				"3 1 5",
				"3 4 4",
				"4 3 2"
		]
		graph = [[INF] * (n + 1) for _ in range(n + 1)]

		# 자기 자신에서 자기 자신으로 가는 비용은 0
		for a in range(1, n + 1):
				graph[a][a] = 0

		# 각 간선에 대한 정보로 초기화
		for row in input_graph:
				a, b, c = map(int, row.split())
				graph[a][b] = c

		"""플로이드 워셜 알고리즘 수행"""
		for k in range(n + 1):  # 모든 노드를 한 바뀌씩 돌면서
				for a in range(n + 1):  # a에서 출발하여
						for b in range(n + 1):  # b로 도착할 때 k 노드를 거쳐가는 경우와 그렇지 않은 경우 중 작은 수로 결정
								graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

		# 출력
		for i in range(n + 1):
				graph[i] = list(map(lambda x: -1 if x == INF else x, graph[i]))
		ret = [row[1:] for row in graph[1:]]
		print(ret)
