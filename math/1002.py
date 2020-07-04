n = int(input())
a = b = [0]*3
for _ in range(n):
    l = list(map(int, input().split()))
    a, b = l[:3], l[3:]
    d = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)
    m = max(a[2],b[2])
    n = min(a[2],b[2])
    if d == 0 and m == n:
        print(-1)
    elif d == m+n or m==d+n:
        print(1)
    elif d > m+n or m > d+n:
        print(0)
    else:
        print(2)
