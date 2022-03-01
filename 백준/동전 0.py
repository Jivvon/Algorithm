import sys

n, k = map(int, sys.stdin.readline().split())
coins = []

for _ in range(n):
    coins.append(int(sys.stdin.readline()))

used_coins = 0
while k:
    a, b = divmod(k, coins.pop())
    if a > 0:
        used_coins += a
        k = b

print(used_coins)
