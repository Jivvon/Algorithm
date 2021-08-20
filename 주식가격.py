from collections import defaultdict
from typing import List

from timer import timer


# 더 좋은 풀이
@timer
def solution(prices: List[int]) -> List[int]:
		stack = []
		answer = [0] * len(prices)
		for i in range(len(prices)):
				if stack != []:
						while stack != [] and stack[-1][1] > prices[i]:
								past, _ = stack.pop()
								answer[past] = i - past
				stack.append([i, prices[i]])
		for i, s in stack:
				answer[i] = len(prices) - 1 - i
		return answer


# 내 풀이
@timer
def _solution(prices: List[int]) -> List[int]:
		"""
		dictionary에 인덱스를 하나씩 가지고 있다가 다음 나오는 값보다 작으면 answer에 입력
		"""
		l = len(prices)
		answer = [0] * l
		dic = defaultdict(list)
		"""
		dic = { value : [ bigger_indexes ] } 
		"""

		for price_index, price in enumerate(prices):
				for bigger_value in list(filter(lambda x: x > price, dic.keys())):
						for bigger_index in dic[bigger_value]:
								answer[bigger_index] = price_index - bigger_index
						dic.pop(bigger_value)
				dic[price].append(price_index)

		for _, indexes in dic.items():
				for index in indexes:
					answer[index] = l - index - 1

		return answer


if __name__ == '__main__':
		print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]
		print(solution([1, 3, 2, 2, 1])) # [4, 1, 2, 1, 0]
		print(solution([1, 1, 1])) # [2, 1, 0]
		print(solution([2, 1, 1])) # [1, 1, 0]
