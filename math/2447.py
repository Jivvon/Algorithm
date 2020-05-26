# 전부 *로 찍은 다음 공백으로 바꾸자

def blank(cnt, x, y):
    if cnt == 1: return
    cnt = cnt // 3

    # start xy, end xy
    sx, ex = x + cnt, x + cnt*2
    sy, ey = y + cnt, y + cnt*2

    for i in range(sx, ex):
        for j in range(sy, ey):
            arr[i][j] = ' '

    blank(cnt, x, y)
    blank(cnt, sx, y)
    blank(cnt, ex, y)

    blank(cnt, x, sy)
    blank(cnt, ex, sy)

    blank(cnt, x, ey)
    blank(cnt, sx, ey)
    blank(cnt, ex, ey)

n = int(input())
arr = [["*"]*n for _ in range(n)]
blank(n, 0, 0)
for el in arr:
    print(''.join(el))
