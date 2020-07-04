t = int(input())
inputs = []
for _ in range(t):
    n = int(input())
    inputs.append(n)
n_max = max(inputs)

# 일단 소수를 구하자
arr = [False, False] + [True] * (n_max - 1)
for i in range(2, n_max+1):
    if arr[i]:
        for j in range(i*2, n_max+1, i):
            arr[j] = False

# 파티션을 구하자
arr = [i for i, el in enumerate(arr) if el]
for n in inputs:
    gap = n
    for i in arr:
        if n-i in arr:
            if gap > abs(n-i*2):
                a = i
                b = n-i
                gap = abs(n-i*2)
    print(a, b)
