import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    stack = deque()
    answer = "YES"
    for s in list(sys.stdin.readline().rstrip()):
        if s == "(":
            stack.append(1)
        elif s == ")":
            if stack:
                stack.pop()
            else:
                answer = "NO"
                break
    if stack:
        answer = "NO"
    print(answer)
