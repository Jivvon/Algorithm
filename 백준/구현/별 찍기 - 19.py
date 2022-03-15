import sys

n = int(sys.stdin.readline().rstrip())
STAR = "*"

w = 4 * n - 3
for i in range(w):
    cur = ""
    k = abs(w // 2 - i)
    m = 4 * (k // 2) + 1
    s = (w - m) // 4
    if k % 2 == 0:
        cur = ((STAR + " ") * s) + (STAR * m) + ((" " + STAR) * s)
    elif k % 2 == 1:
        cur = ((STAR + " ") * s) + (" " * m) + ((" " + STAR) * s)

    print(cur)
