n = int(input())
ff = [0, 1] + [False] * (n - 1)

def fibo(n):
    if ff[n] is not False:
        return ff[n]
    else:
        ff[n] = fibo(n - 2) + fibo(n - 1)
        return ff[n]

print(fibo(n))
