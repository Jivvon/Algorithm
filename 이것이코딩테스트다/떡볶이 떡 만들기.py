from typing import List

from utils.timer import timer


@timer
def solution(arr: List[int], n: int, m: int):
		start = 0
		end = max(arr)
		answer = -1
		while start <= end:
				mid = (start + end) // 2
				bigger_arr = list(filter(lambda x: x > mid, arr))
				total = sum(bigger_arr) - (len(bigger_arr) * mid)
				if total < m:
						end = mid - 1
						continue
				answer = mid
				start = mid + 1
		return answer


if __name__ == '__main__':
		solution([19, 15, 10, 17], 4, 6)
