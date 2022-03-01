from collections import Counter
from functools import reduce
from itertools import combinations
from typing import List

from utils.timer import timer


@timer
def solution(clothes: List[List[str]]) -> int:
		"""
		하의, 상의가 (2, 3)인 경우
		(하의 2개+안입은 경우) * (상의 2개 + 안입은 경우) = 3 * 4 = 12
		그리고 전체에서 -1 (전부다 안입는 경우의 수를 뺀다)
		"""
		answer = 1
		from collections import defaultdict
		dic = defaultdict(list)

		for cloth, Type in clothes:
				dic[Type].append(cloth)

		for Type in dic:
				answer *= len(dic[Type]) + 1

		return answer - 1


def multiply(arr) -> int:
		return reduce(lambda x, y: x * y, arr)


# 시간 초과
@timer
def _solution(clothes: List[List[str]]) -> int:
		"""
		하의, 상의가 (2, 3)인 경우
		하의만 입을 때, 상의만 입을 때, 둘 다 입을 때 경우의 수를 모두 구하여 더한다. (시간초과)
		"""
		answer = 0
		clothes = list(Counter(list(map(lambda x: x[1], clothes))).values())

		for i in range(1, len(clothes) + 1):
				for j in list(combinations(clothes, i)):
						answer += multiply(j)

		return answer


if __name__ == '__main__':
		a = solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])  # 5
		print(a)
		a = solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])  # 3
		print(a)
		a = solution([["2", "3"], ["2", "3"], ["2", "4"], ["2", "4"], ["2", "4"], ["2", "5"], ["2", "5"]])
		print(a)
