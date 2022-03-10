import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())

dic = defaultdict(int)

for _ in range(n):
    dic[sys.stdin.readline().rstrip().split(".")[-1]] += 1

for k, v in list(sorted(dic.items(), key=lambda x: x[0])):
    print(k, v)
