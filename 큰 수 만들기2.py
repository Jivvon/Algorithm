from utils.timer import timer


@timer
def solution(number: str, k: int) -> str:
    from collections import deque
    q = deque()

    for i, v in enumerate(number):
        while q and q[-1] < v and k > 0:
            q.pop()
            k -= 1

        if k == 0:
            q.extend(number[i:])
            break

        q.append(v)

    answers = list(q)[:-k] if k > 0 else list(q)
    return ''.join(answers)


@timer
# 10번만 시간초과
def _solution(number: str, k: int) -> str:
    """
    어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
    예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

    뒤에서부터 len-k개의 숫자만큼 정해놓고
    앞으로 보면서 제일 앞 숫자랑 비교해서 더 크면
    남은 숫자들로 가장 큰 len-k-1 값을 구한다.

    9687351
       7351
      87 51
      87 51
    9 87 5

    """
    numbers = list(number)
    idxs = [i for i in range(k, len(numbers))]

    for i in range(k - 1, -1, -1):
        if numbers[i] < numbers[idxs[0]]:
            continue
        # 현재 보고 있는 값이 첫 번째 값과 같거나 큰 경우
        for j in range(len(idxs)):
            if j == len(idxs) - 1 or numbers[idxs[j]] < numbers[idxs[j + 1]]:
                break
        idxs.pop(j)
        idxs.insert(0, i)

    return "".join([numbers[i] for i in idxs])


if __name__ == '__main__':
    solution("1924", 2)  # 94
    solution("1231234", 3)  # 3234
    solution("4177252841", 4)  # 775841
    solution("7677321", 3)  # 7773
    solution("9687351", 3)  # 9875
    solution("74723961", 4)  # 7961
    solution("988543321099999009", 17)  # 9
