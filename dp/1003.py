import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
dp_0 = [1, 0] + [0] * 40
dp_1 = [0, 1] + [0] * 40
def fibo(n):
    if n < 2 or dp_0[n] or dp_1[n]:
        return (dp_0[n],dp_1[n])
    n2 = fibo(n-2)
    n1 = fibo(n-1)
    dp_0[n] = n2[0] + n1[0]
    dp_1[n] = n2[1] + n1[1]
    return (dp_0[n],dp_1[n])

t = int(input())

for i in range(t):
    n = int(input())
    fibo(n)
    print(dp_0[n], dp_1[n])
