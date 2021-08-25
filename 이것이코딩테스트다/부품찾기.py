from typing import List

from utils.timer import timer


def bi_search(arr: List[int], target: int, start: int, end: int):
		mid = (start + end) // 2
		val = arr[mid][1]
		if start > end:
				return -1
		if val == target:
				return mid
		if target > val:
				return bi_search(arr, target, mid + 1, end)
		elif target < val:
				return bi_search(arr, target, start, mid - 1)


@timer
def solution(n: int, arr: List[int], m: int, targets: List[int]):
		answers = ["no"] * m
		for i, target in enumerate(targets):
				ret = bi_search(list(sorted(enumerate(arr), key=lambda x: x[1])), target, 0, n - 1)
				if ret != -1:
						answers[i] = "yes"
		return ' '.join(answers)


if __name__ == '__main__':
		solution(5, [8, 3, 7, 9, 2], 3, [5, 7, 9])  # no yes yes
