from typing import List

from utils.timer import timer

"""
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.
"""


# class 사용
@timer
def solution(genres, plays):
	answer = []
	dic = {}
	album_list = []
	for i in range(len(genres)):
		dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
		album_list.append(Album(genres[i], plays[i], i))

	dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
	album_list = sorted(album_list, reverse=True)

	while len(dic) > 0:
		play_genre = dic.pop(0)
		print(play_genre)
		cnt = 0;
		for ab in album_list:
			if play_genre[0] == ab.genre:
				answer.append(ab.track)
				cnt += 1
			if cnt == 2:
				break

	return answer


class Album:
	def __init__(self, genre, play, index):
		self.genre = genre
		self.play = play
		self.track = index

	def __lt__(self, other):
		return self.play < other.play

	def __gt__(self, other):
		return self.play > other.play

	def __le__(self, other):
		return self.play <= other.play

	def __ge__(self, other):
		return self.play >= other.play

	def __eq__(self, other):
		return self.play == other.play

	def __ne__(self, other):
		return self.play != other.play


# 내 풀이
@timer
def _solution(genres: List[str], plays: List[int]) -> List[int]:
	"""
    1. 재생수에 인덱스 같이 해서 정렬
    2. tables에 장르별 총합만 가지고 있고 index에는 순서대로 인덱스만 저장
    """
	from collections import defaultdict

	index_of_genre = defaultdict(list)  # {genre: [idx sorted by plays]}
	sum_of_genre = defaultdict(int)  # {genre: sum of plays}

	for idx, val in sorted(enumerate(plays), key=lambda x: x[1], reverse=True):
		index_of_genre[genres[idx]].append(idx)
		sum_of_genre[genres[idx]] += val

	answer = []
	for key, _ in sorted(sum_of_genre.items(), key=lambda x: x[1], reverse=True):
		answer.extend(index_of_genre[key][:2])

	return answer


if __name__ == '__main__':
	_solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])  # [4, 1, 3, 0]
	_solution(["classic", "pop", "classic2", "pop2"], [500, 600, 150, 800])  # [3, 1, 0, 2]
