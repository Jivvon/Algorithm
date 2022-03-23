from collections import Counter


def solution(s):
    count_do, count_0 = 0, 0

    while s != "1":
        nums = Counter(s)
        count_0 += nums["0"]
        s = bin(nums["1"])[2:]
        count_do += 1

    return count_do, count_0


if __name__ == '__main__':
    print(solution("110010101001"))
    print(solution("01110"))
    print(solution("1111111"))
