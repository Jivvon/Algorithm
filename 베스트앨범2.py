from typing import List

from utils.timer import timer


@timer
def solution(genres: List[str], plays: List[int]):
    """
    1. 가장 많이 재생된 장르
    2. 많이 재생된 노래 (같으면 고유번호 낮은순)

    장르별로 index, 재생수 배열 만들어서 정렬하면 될듯
    """
    from collections import defaultdict
    songs = defaultdict(list)  # { classic: [[play, idx], [play, idx]] }

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        songs[genre].append([play, idx])

    sums = []  # [[classic, 100], [pop, 500]]
    for k, v in songs.items():
        sums.append([k, sum([song[0] for song in v])])
    sums = sorted(sums, key=lambda x: x[1], reverse=True)

    answer = []
    for s in sums:
        _top2 = sorted(songs[s[0]], reverse=True)[:2]
        answer.extend([i[1] for i in _top2])

    return answer


if __name__ == '__main__':
    solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
