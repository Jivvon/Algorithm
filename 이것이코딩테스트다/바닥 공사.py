from utils.timer import timer


@timer
def solution(n: int):
		"""
		① 왼쪽부터 i - 1까지 길이가 덮개로 이미 채워져 있으면 2 X 1의 덮개를 채우는 하나의 경우밖에 존재하지 않는다.
		② 왼쪽부터 i - 2까지 길이가 덮개로 이미 채워져 있으면 1 X 2 덮개 2개를 넣는 경우, 혹은 2 X 2의 덮개 하나를 넣는 경우로 2가지 경우가 존재한다.

		여기에서 ②에서 2 X 1 덮개 2개를 넣는 경우를 고려하지 않는 이유는 ①에서 이미 해당 경우가 계산되었기(고려되었기) 때문이다.
		"""
		dp = [0] * (n + 1)
		dp[1] = 1
		dp[2] = 3
		for i in range(3, n + 1):
				dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 796796
		return dp[n]


if __name__ == '__main__':
		solution(3)  # 5
