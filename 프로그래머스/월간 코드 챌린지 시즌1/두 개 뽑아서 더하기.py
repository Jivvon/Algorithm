from itertools import combinations


def solution(numbers):
    return list(sorted(set(map(sum, combinations(numbers, 2)))))


if __name__ == '__main__':
    print(solution([2, 1, 3, 4, 1]))
    print(solution([5, 0, 2, 7]))
