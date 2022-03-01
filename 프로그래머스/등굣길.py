from typing import List

from utils.timer import timer


# 재귀 사용
@timer
def solution(m, n, puddles):
		info = dict([
				((2, 1), 1),
				((1, 2), 1),
		])
		for p in puddles:
				info[tuple(p)] = 0

		def func(m, n):
				if m < 1 or n < 1:
						return 0
				if (m, n) in info:
						return info[(m, n)]
				return info.setdefault((m, n), func(m - 1, n) + func(m, n - 1))

		return func(m, n) % 1000000007


# 내 풀이
@timer
def _solution(m: int, n: int, puddles: List[List[int]]):
		dp = [[1] * m for _ in range(n)]

		for i in puddles:
				dp[i[1] - 1][i[0] - 1] = 0
				if i[0] == 1:
						for j in range(i[1] - 1, n):
								dp[j][0] = 0
				if i[1] == 1:
						for j in range(i[0] - 1, m):
								dp[0][j] = 0

		for j in range(1, n):
				for i in range(1, m):
						if dp[j][i] != 0:
								dp[j][i] = (dp[j - 1][i] + dp[j][i - 1]) % 1000000007
		return dp[-1][-1]


if __name__ == '__main__':
		solution(4, 3, [[2, 2]])
		solution(4, 3, [[1, 0], [0, 1]])  # 0
		solution(4, 3, [[1, 0], [1, 1], [1, 2], [1, 3]])  # 0
