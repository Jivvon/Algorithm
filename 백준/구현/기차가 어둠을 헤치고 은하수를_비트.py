import sys

n, m = map(int, sys.stdin.readline().split())
train = [0] * (n + 1)

for _ in range(m):
    cmd = list(map(int, sys.stdin.readline().split()))
    if cmd[0] == 1:
        train[cmd[1]] = train[cmd[1]] | (1 << cmd[2])
    elif cmd[0] == 2:
        train[cmd[1]] = train[cmd[1]] & ~(1 << cmd[2])
    elif cmd[0] == 3:
        train[cmd[1]] = train[cmd[1]] << 1
        train[cmd[1]] = train[cmd[1]] & ((1 << 21) - 1)
    else:
        train[cmd[1]] = train[cmd[1]] >> 1
        train[cmd[1]] = train[cmd[1]] & ~1

train = list(set(train[1:]))
print(len(train))
