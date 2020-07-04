import sys
n = int(sys.stdin.readline())

first = 1
second = 2
for i in range(n-1):
    first, second = second, first
    second = (first + second) % 15746
print(first)

# 1   1
# 2   00 11
# 3   001 100 111
# 5   0000 0011 1001 1100 1111
# 8   00001 00100 10000 00111 10011 11001 11100 11111
