def solution(a: list):
    length = len(a)
    sort_a = list(sorted(enumerate(a), key=lambda x: x[1]))
    i = j = sort_a[0][0]
    answer = 0
    for idx, _ in sort_a:
        if i == 0 and j == length - 1:
            break
        if idx < i:
            if i - idx > 1:
                answer += i - idx - 1
            i = idx
        elif idx > j:
            if idx - j > 1:
                answer += idx - j - 1
            j = idx
    return length - answer


if __name__ == '__main__':
    print(solution([9, -1, -5]))
    print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
