import sys
input = lambda :sys.stdin.readline()

def sol(k, res, add, sub, mul, div):
    global max_, min_
    if k == n:
        if max_ < res:
            max_ = res
        if min_ > res:
            min_ = res

    if add:
        sol(k+1, res+arr[k], add-1, sub, mul, div)
    if sub:
        sol(k+1, res-arr[k], add, sub-1, mul, div)
    if mul:
        sol(k+1, res*arr[k], add, sub, mul-1, div)
    if div:
        sol(k+1, int(res/arr[k]), add, sub, mul, div-1)

if __name__ == '__main__':
    max_, min_ = -1e9, 1e9
    n = int(input())
    arr = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())
    sol(1, arr[0], add, sub, mul, div)

    print(max_)
    print(min_)
