from typing import List

from utils.timer import timer


@timer
def solution(n: int, k: List[int]):
		dp = [0] * n
		dp[0] = k[0]
		dp[1] = max(k[0], k[1])
		for i in range(2, n):
				dp[i] = max(dp[i - 2] + k[i], dp[i - 1])
		print('dp: {}'.format(dp))
		return max(dp[-2:])


if __name__ == '__main__':
		solution(4, [1, 3, 1, 5])  # 8
