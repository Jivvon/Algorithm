def solution():
		"""
		n x n 크기의 지도에서 (1,1)에서 시작하여 도착하는 지점의 좌표
		"""
		n = int(input())
		arr = input().split()
		move = {
				'L': (0, -1),
				'R': (0, 1),
				'U': (-1, 0),
				'D': (1, 0)
		}
		cur = [1, 1]

		for i in arr:
				m = move.get(i)
				if 0 < cur[0] + m[0] <= n:
						cur[0] += m[0]
				if 0 < cur[1] + m[1] <= n:
						cur[1] += m[1]

		return '{} {}'.format(*cur)


if __name__ == '__main__':
		ret = solution()
		print(ret)
