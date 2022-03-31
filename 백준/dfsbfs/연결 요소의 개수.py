import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = dict(zip([i for i in range(1, n + 1)], [[] for _ in range(n)]))
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * (n + 1)


def bfs(start):
    if visited[start]:
        return 0
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        visited[cur] = True
        queue.extend(list(filter(lambda x: not visited[x] and x not in queue, arr[cur])))
    return 1


answer = 0
for k, v, in arr.items():
    answer += bfs(k)
print(answer)
