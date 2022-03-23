def solution(n):
    ret = ""
    while n > 0:
        n, r = divmod(n, 3)
        ret += str(r)
    return int(ret, 3)


if __name__ == '__main__':
    print(solution(45))
    print(solution(125))
