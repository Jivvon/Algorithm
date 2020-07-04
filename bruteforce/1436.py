import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
six_n = 666
while True:
    if '666' in str(six_n):
        N -= 1
    if N == 0:
        print(six_n)
        break
    six_n += 1
