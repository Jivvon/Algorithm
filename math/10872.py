n = int(input())

def facrotial(n):
    if n < 2:
        return 1
    else:
        return n * facrotial(n-1)

print(facrotial(n))
