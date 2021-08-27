from typing import List


def find_parent(parent: List[int], x):
		if x != parent[x]:
				parent[x] = find_parent(parent, parent[x])
		return parent[x]


def union_parent(parent: List[int], a, b):
		parent_a, parent_b = find_parent(parent, a), find_parent(parent, b)
		if parent_a < parent_b:
				parent[parent_b] = parent_a
		else:
				parent[parent_a] = parent_b


if __name__ == '__main__':
		v, e = 7, 9  # vertical, edge
		parent = [i for i in range(v + 1)]  # 부모를 자기 자신으로 초기화
		arr = [
				[1, 2, 29],
				[1, 5, 75],
				[2, 3, 35],
				[2, 6, 34],
				[3, 4, 7],
				[4, 6, 23],
				[4, 7, 13],
				[5, 6, 53],
				[6, 7, 25]
		]
		cost_total = 0

		arr.sort(key=lambda x: x[2])
		for a, b, cost in arr:
				if find_parent(parent, a) == find_parent(parent, b):
						continue
				union_parent(parent, a, b)
				cost_total += cost

		print(cost_total)
