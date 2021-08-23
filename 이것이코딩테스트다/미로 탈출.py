from typing import List


def bfs(arr: List[List[int]], n: int, m: int, x:int , y:int):
		from collections import deque
		queue = deque([[x, y]])

		dx = [-1, 1, 0, 0]
		dy = [0, 0, -1, 1]

		while queue:
				cur = queue.popleft()
				for i in range(4):
						nx = cur[0] + dx[i]
						ny = cur[1] + dy[i]
						if (0 <= nx-1 < n and 0 <= ny-1 < m) and arr[nx-1][ny-1] == 1:
								arr[nx - 1][ny - 1] += arr[cur[0]-1][cur[1]-1]
								queue.append([nx, ny])
		return arr[-1][-1]


def solution(arr: List[List[int]], n: int, m: int) -> int:
		return bfs(arr, n, m, 1, 1)


if __name__ == '__main__':
		arr = [
				[1,0,1,0,1,0],
				[1,1,1,1,1,1],
				[0,0,0,0,0,1],
				[1,1,1,1,1,1],
				[1,1,1,1,1,1]
		]
		ret = solution(arr, 5, 6)
		print(ret)
