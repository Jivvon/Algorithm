import sys, itertools
input = sys.stdin.readline
N = int(input())

answer = 0
for i in range(N//2):
    for j in itertools.product(range(N-(i*2)+1), repeat=i+1):
        if sum(j) == N-(i*2):
            answer += 1
            # print(j)
if N % 2 == 0:
    answer += 1
elif N % 2 == 1:
    answer += N // 2 + 1

print(answer)
