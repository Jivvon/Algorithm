from typing import List


def dfs(graph: List[List[int]], v: int, visited: List[bool]):
		visited[v] = True
		print(v, end=' ')

		for i in graph[v]:
				if not visited[i]:
						dfs(graph, i, visited)


def solution():
		graph = [
				[],
				[2, 3, 8],
				[1, 7],
				[1, 4, 5],
				[3, 5],
				[3, 4],
				[7],
				[2, 6, 8],
				[1, 7]
		]
		start = 1
		visited = [False] * len(graph)

		dfs(graph, start, visited)


if __name__ == '__main__':
		solution()
