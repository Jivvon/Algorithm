from sys import stdin
n = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(n)]
arr = list(map(list, zip(arr,arr)))

if n > 1: arr[1][1] += arr[0][0]

for i in range(2,n):
    arr[i][0] += max(arr[i-2])
    arr[i][1] += arr[i-1][0]

print(max(arr[-1]))
