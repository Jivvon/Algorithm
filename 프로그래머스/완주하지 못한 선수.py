import collections
from typing import List


def _solution(participant: List[str], completion: List[str]) -> str:
    a = collections.Counter(participant)
    b = collections.Counter(completion)
    answer = list((a - b).keys())[0]
    return answer


def solution(participant: List[str], completion: List[str]) -> str:
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
        print(temp)
    for com in completion:
        temp -= int(hash(com))
        print(temp)
    answer = dic[temp]

    return answer


if __name__ == '__main__':
    a = solution(["mislav", "stanko", "mislav", "ana"]	, ["stanko", "ana", "mislav"]	) # "mislav"
    print(a)
