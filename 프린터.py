from typing import List


def solution(priorities: List[int], location: int) -> int:
    priorities[location+1:]
    print(priorities[location+1:])
    answer = len(list(filter(lambda x: priorities[location] < x, priorities[location+1:])))
    return answer


if __name__ == '__main__':
    a = solution([2, 1, 3, 2]	,2)
    print(a) # == 1
    a = solution([1, 1, 9, 1, 1, 1]	,0)
    print(a) # == 5

