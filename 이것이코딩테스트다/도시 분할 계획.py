from typing import List

from utils.timer import timer


def find_neighbor(neighbor: List[int], x):
		if x != neighbor[x]:
				neighbor[x] = find_neighbor(neighbor, neighbor[x])
		return neighbor[x]


def union_house(neighbor: List[int], a, b):
		neighbor_a = find_neighbor(neighbor, a)
		neighbor_b = find_neighbor(neighbor, b)
		if neighbor_a < neighbor_b:
				neighbor[neighbor_b] = neighbor_a
		else:
				neighbor[neighbor_a] = neighbor_b


@timer
def solution(n, m, arr: List[List[int]]):
		"""
		n 개의 집과 m 개의 길 1e5, 1e6
		방향 x 비용 o
		마을 2개로 분리
		각 마을 안에는 모두 연결되어 있어야 함
		길 비용이 최소가 되어야 함

		비용이 최소가 되도록 마을을 하나 만들고, 가장 비용이 큰 간선부터 지우자
		"""
		neighbor = [i for i in range(n + 1)]
		arr.sort(key=lambda x: x[2])
		total_cost = 0
		max_cost = 0

		for a, b, cost in arr:
				if find_neighbor(neighbor, a) == find_neighbor(neighbor, b):
						continue
				union_house(neighbor, a, b)
				total_cost += cost
				max_cost = max(max_cost, cost)

		return total_cost - max_cost


if __name__ == '__main__':
		n, m = 7, 12
		arr = [  # [0]과 [1]을 연결하는데 드는 비용 [2]
				[1, 2, 3],
				[1, 3, 2],
				[3, 2, 1],
				[2, 5, 2],
				[3, 3, 4],
				[7, 3, 6],
				[5, 1, 5],
				[1, 6, 2],
				[6, 4, 1],
				[6, 5, 3],
				[4, 5, 3],
				[6, 7, 4]
		]
		solution(n, m, arr)
