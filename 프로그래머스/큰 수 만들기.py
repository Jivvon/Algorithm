"""
2:27 ~ 1+a..
"""
from utils.timer import timer


# 10번만 시간초과
@timer
def solution(number: str, k: int):
		"""
		인덱스로 접근해보자
		74723961 일 때
		    3961
		    3961
		  7  961
		  7  961
		7 7  96
		로 바뀌어야 한다
		7298692
		   8692
		  98 92
		  98 92

		큐 사용하자
		"""
		answers = list(number[n] for n in range(k, len(number), 1))
		for i in range(k - 1, -1, -1):
				if number[i] >= answers[0]:
						for j in range(len(answers) - 1):
								if answers[j] == 9:
										break
								if answers[j] < answers[j + 1]:
										answers.pop(j)
										break
						answers = [number[i]] + answers
		answers = answers[:len(number) - k]
		return ''.join(answers)


# 시간초과
@timer
def _solution(number: str, k: int):
		from itertools import combinations
		numbers = list(number)
		arr = list(combinations(numbers, len(numbers) - k))
		answer = ''.join(sorted(arr, reverse=True)[0])

		return answer


if __name__ == '__main__':
		solution("1924", 2)  # 94
		solution("1231234", 3)  # 3234
		solution("4177252841", 4)  # 775841
		solution("7677321", 3)  # 7773
		solution("74723961", 4)  # 7961
		solution("988543321099999009", 17)  # 9
