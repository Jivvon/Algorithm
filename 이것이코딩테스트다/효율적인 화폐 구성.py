from typing import List

from utils.timer import timer


@timer
def solution(n: int, m: int, arr: List[int]):
		# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
		d = [10001] * (m + 1)

		# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
		d[0] = 0
		for i in range(n):
				for j in range(arr[i], m + 1):
						if d[j - arr[i]] != 10001:  # (i - k)원을 만드는 방법이 존재하는 경우
								d[j] = min(d[j], d[j - arr[i]] + 1)

		# 계산된 결과 출력
		if d[m] == 10001:  # 최종적으로 M원을 만드는 방법이 없는 경우
				print(-1)
		else:
				print(d[m])


# 내 풀이
@timer
def _solution(n: int, m: int, arr: List[int]):
		DEFAULT_VALUE = 10001
		d = [DEFAULT_VALUE] * (m + 1)

		for i in range(1, m + 1):
				if i in arr:
						d[i] = 1
						continue
				# i보다 작은 것들만큼 뺀 곳 + 1을 더해서 가장 작은 것
				for j in list(filter(lambda x: x < i, arr)):
						d[i] = min(d[i], d[i - j] + 1)

		if d[m] == DEFAULT_VALUE:
				return -1
		return d[m]


if __name__ == '__main__':
		solution(2, 15, [2, 3])  # 5
		solution(3, 4, [3, 5, 7])  # -1
