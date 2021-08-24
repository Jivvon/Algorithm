"""
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
입출력 예
numbers	return
"17"	3
"011"	2
입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

11과 011은 같은 숫자로 취급합니다.
"""

from utils.timer import timer


# 좋아요 많이 받은 풀이
@timer
def solution(numbers: str) -> int:
		from itertools import permutations
		a = set()
		for i in range(len(numbers)):
				a |= set(map(int, map("".join, permutations(list(numbers), i+1))))
		a -= set(range(0, 2)) # 0, 1 제외
		for i in range(2, int(max(a) ** 0.5) + 1): # 2부터 제곱근 a까지
				a -= set(range(i * 2, max(a) + 1, i)) # i에 가장 작은 소수(2)를 곱한 수부터 제외
		return len(a)


def _is_prime_number(n: int):
		"""소수 판별"""
		from math import sqrt

		if n == 0 or n == 1:
				return False
		for i in range(2, int(sqrt(n)) + 1):
				if n % i == 0:
						return False
		return True


# 내 풀이
@timer
def _solution(numbers: str) -> int:
		from itertools import permutations

		nums = list(map(int, list(numbers)))
		answer = 0

		arr = []
		for i in range(1, len(nums) + 1):
				num_comb = list(map(lambda x: x, list(permutations(nums, i))))
				arr.extend(list(map(lambda x: int(''.join(map(str, x))), set(num_comb))))

		arr = set(arr)
		answer += len(list(filter(lambda x: _is_prime_number(x), arr)))

		return answer


if __name__ == '__main__':
		solution("17") # 3
		solution("011") # 2
