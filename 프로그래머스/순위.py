"""못 풀어서 다른 풀이 참고"""

from typing import List

from utils.timer import timer


@timer
def solution(n: int, results: List[List[int]]) -> int:
		from collections import defaultdict

		win, lose = defaultdict(set), defaultdict(set)
		answer = 0
		for result in results:
				lose[result[1]].add(result[0])
				win[result[0]].add(result[1])

		for i in range(1, n + 1):
				for winner in lose[i]:
						win[winner].update(win[i])
				for loser in win[i]:
						lose[loser].update(lose[i])

		for i in range(1, n + 1):
				if len(win[i]) + len(lose[i]) == n - 1:
						answer += 1
		return answer


@timer
def _solution(n: int, results: List[List[int]]) -> int:
		"""
		[0]이 [1]에 이겼을 때에는 1
		[0]이 [1]에 졌을 때에는 -1
		[0]이 [1]의 관계를 모를 때에는 0
		"""
		board = [[0] * (n + 1) for _ in range(n + 1)]
		for p1, p2 in results:
				board[p1][p2] = 1
				board[p2][p1] = -1

		for k in range(n + 1):
				for i in range(n + 1):
						for j in range(n + 1):
								if board[i][k] == 1 and board[k][j] == 1:
										board[i][j] = 1
								elif board[i][k] == -1 and board[k][j] == -1:
										board[i][j] = -1

		from collections import Counter
		answer = 0
		for i in range(1, n + 1):
				if Counter(board[i][1:]).get(0) == 1:
						answer += 1

		return answer


if __name__ == '__main__':
		solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])  # 2
