"""
union-find 에서
마지막에 부모를 가리키지 않는 반례도 존재하기 때문에
부모를 가리키도록 한번 순회하여야 한다
```
for i in range(n):
		parent[i] = find_parent(parent, i)
```
"""
from utils.timer import timer


# queue
@timer
def solution(n, computers):
		from collections import deque
		queue = deque()
		visited = [0] * n
		queue.append(0)  # start

		answer = 0
		while 0 in visited:  # 가보지 않은 곳이 있을 때까지
				queue.append(visited.index(0))
				while queue:
						cur = queue.popleft()
						for i in range(n):
								if computers[cur][i] == 1 and visited[i] == 0:
										visited[i] = 1
										queue.append(i)
				answer += 1
		return answer


# union-find
def find_parent(parent, n):
		if parent[n] != n:
				parent[n] = find_parent(parent, parent[n])
		return parent[n]


def union(parent, a, b):
		_a = find_parent(parent, a)
		_b = find_parent(parent, b)
		if _a < _b:
				parent[_b] = _a
		else:
				parent[_a] = _b
		return parent


@timer
def _solution(n, computers):
		parent = [i for i in range(n)]
		for row in range(len(computers)):
				for col in range(len(computers)):
						if row != col and computers[row][col] == 1:
								union(parent, row, col)

		for i in range(n):
				parent[i] = find_parent(parent, i)

		answer = len(set(parent))
		return answer


if __name__ == '__main__':
		# solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])  # 2
		# solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])  # 1
		solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # 3
		solution(4, [[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 1], [0, 0, 1, 1]])  # 1
# solution(4, [[1, 1, 0, 0], [1, 1, 1, 1], [0, 1, 1, 0], [0, 1, 0, 1]])  # 1
# solution(4, [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]])  # 2
# solution(1, [[1]])  # 1
# solution(2, [[1, 0], [0, 1]])  # 2
