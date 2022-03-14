import sys

n = int(sys.stdin.readline().rstrip())

dic = dict()
answer = 0
for _ in range(n):
    cow, pos = map(int, sys.stdin.readline().rstrip().split())
    if cow not in dic.keys():
        dic[cow] = pos
    elif dic[cow] != pos:
        dic[cow] = pos
        answer += 1

print(answer)
