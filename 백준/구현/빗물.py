import sys

h, w = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

answer = 0
for i in range(1, w - 1):
    tmp = min(max(arr[:i]), max(arr[i + 1:]))
    if tmp > arr[i]:
        answer += tmp - arr[i]

print(answer)
