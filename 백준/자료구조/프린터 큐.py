import sys
from collections import deque, Counter

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    priors = list(map(int, sys.stdin.readline().rstrip().split()))
    counter = Counter(priors)
    q = deque(enumerate(priors))
    count = 0
    while q:
        i, prior = q.popleft()
        if any(prior < i for i in counter.keys()):
            q.append((i, prior))
            continue
        count += 1
        if i == m:
            break
        counter[prior] -= 1
        if not counter[prior]:
            counter.pop(prior)
    print(count)
