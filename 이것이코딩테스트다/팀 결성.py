from typing import List

from utils.timer import timer


def find_leader(leaders: List, x: int):
		if x != leaders[x]:
				leaders[x] = find_leader(leaders, leaders[x])
		return leaders[x]


def union_teams(leaders: List, a, b):
		leader_a = find_leader(leaders, a)
		leader_b = find_leader(leaders, b)
		if leader_a < leader_b:
				leaders[b] = a
		else:
				leaders[a] = b


@timer
def solution(n, m, arr: List[List[int]]):
		"""
		:param n: 0 ~ n번까지 번호를 부여하여 학생은 총 n+1명
		:param m: 연산의 개수
		:param arr: 입력
		:return: 같은 팀 여부 확인 연산에 대한 연산 결과를 NO, YES로 줄 바꿔서 출력
		"""
		leaders = [i for i in range(n + 1)]
		for operator, a, b in arr:
				if operator == 0:
						union_teams(leaders, a, b)
				elif operator == 1:
						print("YES" if find_leader(leaders, a) == find_leader(leaders, b) else "NO")


if __name__ == '__main__':
		n, m = 7, 8
		arr = [
				[0, 1, 3],
				[1, 1, 7],
				[0, 7, 6],
				[1, 7, 1],
				[0, 3, 7],
				[0, 4, 2],
				[0, 1, 1],
				[1, 1, 1]
		]
		solution(n, m, arr)
