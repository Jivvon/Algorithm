inputs = []
while True:
    input_str = int(input())
    if input_str == 0:
        break
    else:
        inputs.append(input_str)

n_max = max(inputs)
arr = [False, False] + [True] * (n_max * 2 - 1)

for i in range(2, 2 * n_max + 1):
    if arr[i]:
        for _ in range(i*2, 2 * n_max + 1, i):
            arr[_] = False

for n in inputs:
    count = 0
    for i in range(n+1, 2*n+1):
        if arr[i]:
            count += 1
    print(count)
