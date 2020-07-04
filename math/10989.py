# 정렬하려는 수의 범위가 적을 경우에는 counting한다.
import sys

n = int(sys.stdin.readline())
arr = [0] * 10001

for _ in range(n):
    arr[int(sys.stdin.readline())] += 1
for i in range(10001):
    if arr[i] > 0:
        for j in range(arr[i]):
            print(i)
