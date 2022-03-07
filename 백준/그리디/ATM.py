## 숏코딩 72ms
# input()
# print(sum(list(map(lambda x: x[1] * (x[0] + 1), enumerate(sorted(list(map(int, input().split())), reverse=True))))))

## 내 풀이
import sys

N = int(sys.stdin.readline().rstrip())
arr = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)
total = sum(arr)

answer = 0
for i in arr:
    answer += total
    total -= i

print(answer)
