"""
10:10 ~ 11:12
문제 풀기는 했는데
		solution("ABBAAAAAAAAAB")  # 7
		solution("BABAAAAB")  # 7
해당 두 경우에서 답이 7 대신 8이 나옴
(오른쪽 끝에서 왼쪽으로 넘어갈 수 있으면 7이 맞고, 안 된다면 8이 맞다)
"""
from utils.timer import timer


@timer
def solution(name: str):
		count = list(map(lambda x: ord(x) - ord('A'), list(name)))
		gap = ord('Z') - ord('A') + 1
		for i in range(len(count)):
				count[i] = min(count[i], gap - count[i])

		move = list(set(range(len(count))) & set([i for i, x in enumerate(count) if x != 0]))
		move_count = max(move)
		for i, m in enumerate(move[:-1]):
				move_count = min(move_count, 2 * m + (len(count) - move[i + 1]))

		answer = sum(count) + move_count
		return answer


if __name__ == '__main__':
		solution("BBAAABAB")  # 5 + 4 = 9
		solution("JEROEN")  # 56
		solution("JAN")  # 23
		solution("ABBAAAAAAAAAB")  # 7
		solution("BABAAAAB")  # 7
