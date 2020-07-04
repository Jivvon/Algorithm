m = int(input())
n = int(input())

arr = []
if m == 1:
    if n != 1:
        arr.append(2)
        m = 3

for i in range(m, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break
        if j == i - 1:  # 소수이다
            arr.append(i)

if sum(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])
