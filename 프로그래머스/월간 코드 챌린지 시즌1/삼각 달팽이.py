def fill_border(arr, x, y, s, n):
    l = n - 1 - 3 * x
    if l == 0:
        arr[y][x] = s
        return s + 1
    for i in range(y, y + l):
        arr[i][x] = s
        s += 1
    for i in range(x, x + l):
        arr[y + l][i] = s
        s += 1
    for i in range(l):
        arr[y + l - i][x + l - i] = s
        s += 1
    return s


def solution(n):
    arr = [[0] * i for i in range(1, n + 1)]
    s = 1
    for i in range(n, 0, -2):
        s = fill_border(arr, (n - i) // 2, n - i, s, n)
    # answer = []
    # for a in arr:
    #     answer.extend(a)
    return sum(arr, [])


if __name__ == '__main__':
    print(solution(4))
    print(solution(5))
    print(solution(6))
