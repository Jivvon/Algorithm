def solution(a, b):
    return sum(list(map(lambda x: x[0] * x[1], zip(a, b))))


if __name__ == '__main__':
    print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
