import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.reverse()
count = 0

for num in nums:
    this_count, k = divmod(k, num)
    count += this_count
    if k == 0: break

print(count)
