from utils.timer import timer


def cal_arr(arr1: set, arr2: set):
		ret = set()
		for i in arr1:
				for j in arr2:
						ret.add(i + j)
						ret.add(i - j)
						ret.add(j - i)
						ret.add(i * j)
						if j != 0:
							ret.add(i // j)
						if i != 0:
							ret.add(j // i)
		return ret


@timer
def solution(n: int, number: int):
		"""
		C1 = N
		C2 = NN, N+N, N-N, N*N, N//N
		C3 = NNN, C1+C2, C1-C2, C2-C1, C1*C2, C1//C2, C2//C1
		...
		"""
		if n == number:
				return 1

		answers = [{n}] # C1
		for i in range(2, 9):
				answer = {int(str(n) * i)}
				for j in range(1, i // 2 + 1):
						k = i - j
						answer |= cal_arr(answers[j-1], answers[k-1])
				if number in answer:
						return i
				answers.append(answer)

		return -1


if __name__ == '__main__':
		solution(5, 12) # 4
		solution(2, 11) # 3
		solution(8, 53) # 5

