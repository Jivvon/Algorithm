import sys

n = int(sys.stdin.readline().rstrip())
arr_n = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
arr_m = list(map(int, sys.stdin.readline().rstrip().split()))

arr_n.sort()


def has_k(arr, k):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == k:
            return 1
        elif arr[mid] < k:
            start = mid + 1
        else:
            end = mid - 1
    return 0


for i in arr_m:
    print(has_k(arr_n, i))
