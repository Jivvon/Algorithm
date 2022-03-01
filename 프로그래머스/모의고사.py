"""
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
입출력 예
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
"""
from typing import List

from utils.timer import timer


class Student:
		def __init__(self, pattern: List[int]):
				self.pattern = pattern
				self.length = len(pattern)

		def solve(self, problem: List[int]) -> int:
				return len(list(filter(lambda x: x[1] == self.pattern[x[0] % self.length], enumerate(problem))))


@timer
def solution(answers: List[int]) -> List[int]:
		s1 = Student([1, 2, 3, 4, 5])
		s2 = Student([2, 1, 2, 3, 2, 4, 2, 5])
		s3 = Student([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])

		solve_counts_1 = s1.solve(answers)
		solve_counts_2 = s2.solve(answers)
		solve_counts_3 = s3.solve(answers)
		solve_counts = [solve_counts_1, solve_counts_2, solve_counts_3]

		counts = list(zip(range(1, 4), solve_counts))

		answer = []
		for idx, num in sorted(counts, key=lambda x: x[1], reverse=True):
				if not answer or counts[answer[-1]-1][1] == num:
						answer.append(idx)

		return sorted(answer)


if __name__ == '__main__':
		solution([1,2,3,4,5]) # 1
		solution([1,3,2,4,2]) # 123
		solution([1]) # 1
		solution([1,1,1,1,1]) # 3
		solution([2,2,2,2,2,2]) # 2
		solution([1,1,1]) # 123

