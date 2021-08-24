from typing import List

from utils.timer import timer


# 재귀
@timer
def solution(triangle):
		memo = {}
		answer = f(triangle, 0, 0, memo)
		return answer


def f(triangle, i, j, memo):
		if i == len(triangle) - 1:
				return triangle[i][j]

		if (i, j) in memo:
				return memo[(i, j)]

		a = f(triangle, i + 1, j, memo)
		b = f(triangle, i + 1, j + 1, memo)
		x = triangle[i][j] + max(a, b)

		memo[(i, j)] = x

		return x


# 내 풀이
@timer
def _solution(triangle: List[List[int]]):
		answer = [[triangle[0][0]]]
		for i in range(1, len(triangle)):
				row = triangle[i]
				accumulated_row = []
				for j, el in enumerate(row):
						if j == 0:
								accumulated_row.append(el + answer[i - 1][j])
						elif 0 < j < len(row) - 1:
								accumulated_row.append(el + max(answer[i - 1][j - 1], answer[i - 1][j]))
						elif j == len(row) - 1:
								accumulated_row.append(el + answer[i - 1][j - 1])
				answer.append(accumulated_row)
		return max(answer[-1])


if __name__ == '__main__':
		ret = solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
		print(ret)
