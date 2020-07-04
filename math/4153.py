while True:
    x, y, z = map(int,input().split())
    if x == y == z == 0:
        break
    m = max(x, y, z)
    result = (m ** 2) * 2 == x**2 + y**2 + z**2
    if result:
        print("right")
    else:
        print("wrong")
