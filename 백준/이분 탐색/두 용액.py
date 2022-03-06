N = int(input())
arr = list(map(int, input().split()))
arr.sort()

l, r = 0, N - 1
answer = int(1e10)
final = []

while l < r:
    total = arr[l] + arr[r]
    if abs(total) < answer:
        answer = abs(total)
        final = [arr[l], arr[r]]

    if total < 0:
        l += 1
    else:
        r -= 1

print(*final)
