from typing import List


def bfs(arr: List[List[int]], n: int, m:int , i: int, j: int):
		"""

		:param arr: 얼음 틀
		:param i: 세로 인덱스
		:param j: 가로 인덱스
		"""
		from collections import deque
		queue = deque([[i, j]])

		# 상 하 좌 우
		dx = [-1, 1, 0, 0]
		dy = [0, 0, -1, 1]

		while queue:
				x = queue.popleft()
				arr[x[0]][x[1]] = 1
				for i in range(4):
						nx = x[0] + dx[i]
						ny = x[1] + dy[i]
						if (0 <= nx < n and 0 <= ny < m) and arr[nx][ny] == 0:
								queue.append([nx, ny])


def solution(arr: List[List[int]], n: int, m: int):
		"""
		arr 을 쭉 돌면서 0인 부분에서 bfs를 하자
		bfs에서는 arr으로 0이 오면 방문한 곳은 1로 바꾸자
		"""
		answer = 0

		for i, _arr in enumerate(arr):
				for j, __arr in enumerate(_arr):
						if __arr == 0:
								bfs(arr, n, m, i, j)
								answer += 1

		return answer


if __name__ == '__main__':
		arr = [
				[0,0,1,1,0],
				[0,0,0,1,1],
				[1,1,1,1,1],
				[0,0,0,0,0]
		]
		ret = solution(arr, 4, 5)
		print(ret)
