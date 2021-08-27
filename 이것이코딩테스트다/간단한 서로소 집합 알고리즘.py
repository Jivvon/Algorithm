# 최악의 경우 O(N)
def _find_parent(parent, x):
		"""
		특정 원소가 속한 집합 찾기
		"""
		if parent[x] != x:
				return find_parent(parent, parent[x])
		return x


# 경로 압축
def find_parent(parent, x):
		"""
		특정 원소가 속한 집합 찾기
		"""
		if parent[x] != x:
				parent[x] = find_parent(parent, parent[x])
		return parent[x]


def union_parent(parent, a, b):
		"""
		두 원소가 속한 집합을 합치기
		"""
		a = find_parent(parent, a)
		b = find_parent(parent, b)
		if a < b:
				parent[b] = a
		else:
				parent[a] = b


if __name__ == '__main__':
		v, e = 6, 4,  # vertex, edge
		arr = [
				[1, 4],
				[2, 3],
				[2, 4],
				[5, 6]
		]

		parent = [0] * (v + 1)
		# 1. 부모 테이블을 모두 자기 자신으로 초기화
		for i in range(1, v + 1):
				parent[i] = i

		# 2. union 연산 진행
		for a, b in arr:
				union_parent(parent, a, b)

		# 3. 각 원소가 속한 집합
		for i in range(1, v + 1):
				print(find_parent(parent, i), end=' ')
		print()

		# 부모 테이블
		print(*parent[1:])
