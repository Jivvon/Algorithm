m, n = map(int, input().split())
arr = [False, False] + [True] * (1000000 - 1)

for i, el in enumerate(arr):
    if el:
        for _ in range(i*2, 1000000, i):
            arr[_] = False

for i in range(m, n+1):
    if arr[i]:
        print(i)
