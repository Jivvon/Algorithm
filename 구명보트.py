from typing import List

from utils.timer import timer


@timer
def solution(people: List[int], limit: str):
	people.sort()
	i = 0
	j = len(people) - 1
	answer = 0

	while i < j:
		if people[i] + people[j] <= limit:
			i += 1
		j -= 1
		answer += 1

	if i == j:
		answer += 1

	return answer


if __name__ == '__main__':
	solution([70, 50, 80, 50], 100)  # 3
	solution([70, 50, 80], 100)  # 3
