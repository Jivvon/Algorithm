def hanoi(n, _from, _to, _other):
    if n < 2: # n == 1일 땐 바로 from에서 to로 이동
        print(_from, _to)
        return
    hanoi(n-1, _from, _other, _to) # 가장 큰 원판을 제외한 나머지 원판을 other로 이동
    print(_from, _to)              # 가장 큰 원판 to로 이동
    hanoi(n-1, _other, _to, _from) # other로 이동했던 원판을 to로 이동

n = int(input())
print((2**n)-1) # hanoi 안에서 hanoi를 2번씩 출력하고 n == 1일 땐 한번 출력하므로 (2^n)-1
hanoi(n, 1, 3, 2)
