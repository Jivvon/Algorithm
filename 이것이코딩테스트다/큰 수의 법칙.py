import sys


def solution():
		n, m, k = map(int, sys.stdin.readline().split())
		arr = list(map(int, sys.stdin.readline().split()))

		max_num_1, max_num_2 = sorted(arr, reverse=True)[:2]

		a, b = divmod(m, k + 1)
		answer = a * (max_num_1 * k + max_num_2) + b * max_num_2

		return answer


if __name__ == '__main__':
		ret = solution()
		print(ret)

