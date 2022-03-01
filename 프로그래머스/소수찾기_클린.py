"""라이브러리 하나도 안 쓰고 푼 풀이"""


def check_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    for i in range(2, int(n ** 0.5) + 1):
        if (n % i) == 0:
            return False

    return True


def permutation(base, array, number_set):
    """라이브러리 없이 순열"""
    if base:
        number_set.add(int(base))

    for i, s in enumerate(array):
        permutation(base + s, array[:i] + array[i+1:], number_set)


def solution(numbers):
    number_set = set()
    permutation("", list(numbers), number_set)
    print(number_set)
    answer = len(list(filter(check_prime, number_set)))
    return answer


if __name__ == '__main__':
    # print(solution("17")) # 3
    # print(solution("011")) # 2
    print(solution("123"))

