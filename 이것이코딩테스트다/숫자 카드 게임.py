def solution():
		n, m = map(int, input().split())
		arr = [list(map(int, input().split())) for _ in range(n)]

		min_arr = [min(ar) for ar in arr]
		answer = max(min_arr)

		return answer


if __name__ == '__main__':
		ret = solution()
		print(ret)

