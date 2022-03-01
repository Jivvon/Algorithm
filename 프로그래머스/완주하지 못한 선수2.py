from typing import List
from collections import defaultdict

from utils.timer import timer


@timer
def solution(participant: List[str], completion: List[str]):
	hashsum = 0
	dic = {}
	for p in participant:
		dic[hash(p)] = p
		hashsum += int(hash(p))
	for c in completion:
		hashsum -= hash(c)
	answer = dic[hashsum]
	return answer


if __name__ == '__main__':
	q1 = solution(["mislav", "stanko", "mislav", "ana"]	, ["stanko", "ana", "mislav"]	) # "mislav"
	print(q1)
