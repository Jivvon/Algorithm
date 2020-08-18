arr = input().split('-')
answer = sum(map(int, arr[0].split('+')))
for ar in arr[1:]:
    answer -= sum(map(int, ar.split('+')))
print(answer)
    