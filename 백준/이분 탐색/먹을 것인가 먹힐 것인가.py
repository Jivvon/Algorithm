import sys


def binary_search(arr, target, start: int, end: int):
    res = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res + 1


test_case = int(input())

for _ in range(test_case):
    N, M = map(int, input().split())
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    B = list(map(int, sys.stdin.readline().rstrip().split()))
    answer = 0

    B.sort()
    for a in A:
        answer += binary_search(B, a, 0, M - 1)
    print(answer)
