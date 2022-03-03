from collections import deque

N, K = map(int, input().split())
MIN_POS, MAX_POS = 0, 100000


def bfs(start, target):
    queue = deque([start])
    counts = [0] * (MAX_POS + 1)

    while queue:
        cur = queue.popleft()
        if cur == target:
            answer = counts[cur]
            break
        for i in (cur + 1, cur - 1, cur * 2):
            if MIN_POS <= i <= MAX_POS and (counts[i] == 0 or counts[cur] + 1 < counts[i]):
                counts[i] = counts[cur] + 1
                queue.append(i)

    return answer


print(bfs(N, K))
