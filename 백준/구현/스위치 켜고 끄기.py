import sys


def toggle(arr, i):
    arr[i] = 0 if arr[i] == 1 else 1


def boy(arr, num):
    for idx, a in enumerate(arr):
        if idx % num == 0:
            toggle(arr, idx)
    return arr


def girl(arr, num, n):
    i = 0
    while 1 <= num - i and num + i <= n:
        if arr[num - i] != arr[num + i]:
            break
        i += 1
    i -= 1
    for j in range(num - i, num + i + 1):
        toggle(arr, j)
    return arr


def solution():
    n = int(sys.stdin.readline().rstrip())
    arr = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    students_n = int(sys.stdin.readline().rstrip())

    for _ in range(students_n):
        sex, num = map(int, sys.stdin.readline().rstrip().split())
        if sex == 1:
            arr = boy(arr, num)
        elif sex == 2:
            arr = girl(arr, num, n)

    arr = list(map(str, arr))
    if n <= 20:
        print(" ".join(arr[1:]))
    else:
        i = 1
        while n - i >= 20:
            print(" ".join(arr[i:i + 20]))
            i += 20
        print(" ".join(arr[i:]))


if __name__ == '__main__':
    solution()
"""
40
0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1
2
1 3
2 3
"""
