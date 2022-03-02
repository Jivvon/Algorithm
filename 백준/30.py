N = input()

if '0' in N and sum(map(int, list(N))) % 3 == 0:
    print(''.join(sorted(N, reverse=True)))
else:
    print(-1)
