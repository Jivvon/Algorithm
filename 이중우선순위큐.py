from typing import List

from utils.timer import timer

import heapq


def oper(operation, queue):
		op, num = str.split(operation)
		num = int(num)
		if op == "I":
				heapq.heappush(queue, num)
		if op == "D":
				if not queue:
						return queue
				if num < 0:
						heapq.heappop(queue)
				elif num > 0:
						queue = heapq.nlargest(len(queue), queue)[1:]
						heapq.heapify(queue)

		return queue


def solution(operations: List[str]):
		queue = []
		for operation in operations:
				queue = oper(operation, queue)

		if not queue:
				return [0, 0]
		_max = heapq.nlargest(len(queue), queue)[0]
		_min = heapq.heappop(queue)
		return [_max, _min]


if __name__ == '__main__':
		solution(["I 16", "D 1"])
		solution(["I 7", "I 5", "I -5", "D -1"])
		solution(["I 7", "I 5", "I -5", "D -1", "D 1"])
