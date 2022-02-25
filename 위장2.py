from typing import List

from utils.timer import timer

from collections import defaultdict


@timer
def solution(clothes: List[List[str]]):
    dic = defaultdict(int)
    for clothe in clothes:
        dic[clothe[1]] += 1
    answer = 1
    for v in dic.values():
        answer *= (v + 1)
    answer -= 1
    return answer


if __name__ == '__main__':
    solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
    solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])
