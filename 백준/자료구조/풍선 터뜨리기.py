import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
q = deque(enumerate(map(int, sys.stdin.readline().rstrip().split())))
answers = []

while q:
    idx, num = q.popleft()
    answers.append(idx + 1)
    if num > 0:
        q.rotate(-(num - 1))  # 양수에서 1 빼고 반시계로
    else:
        q.rotate(-num)  # 음의 음수니까 시계방향

print(*answers)
