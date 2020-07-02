N = int(input())

def getDividedSum(num):
    return num + sum(map(int,list(str(num))))

for i in range(N):
    if N == getDividedSum(i):
        print(i)
        exit(1)
print(0)
