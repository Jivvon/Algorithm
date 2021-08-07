import math
from typing import List


def _solution(progresses: List[int], speeds: List[int]) -> List[int]:
    answer = [0]
    # arr = list(map(lambda x: math.ceil((100-x[0])/x[1]), zip(progresses, speeds)))
    arr = list(map(lambda x: -((x[0]-100)//x[1]), zip(progresses, speeds)))
    before_num = arr[0]
    for i in arr:
        if before_num >= i:
            answer[len(answer)-1] += 1
        else:
            answer.append(1)
            before_num = i

    return answer


def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]


if __name__ == '__main__':
    a = solution([93, 30, 55]	,[1, 30, 5]	)
    print(a)
    a = solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
    print(a)
