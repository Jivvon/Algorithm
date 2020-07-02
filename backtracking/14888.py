import sys, itertools
input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split())) # +, -, *, /
operator_list = []
for i, operator in enumerate(operators):
    operator_list.extend([i] * operator)
operator_permutations = itertools.permutations(operator_list, len(operator_list))
candidates = []

def cal(a, b, operator):
    if operator == 0:
        return a+b
    elif operator == 1:
        return a-b
    elif operator == 2:
        return a*b
    elif operator == 3:
        if a < 0 and b > 0:
            return (abs(a) // b) * (-1)
        return a//b

for operator_permutation in operator_permutations:
    candidate = cal(numbers[0], numbers[1], operator_permutation[0])
    for i in range(1, N-1):
        candidate = cal(candidate, numbers[i+1], operator_permutation[i])
    candidates.append(candidate)

print(max(candidates))
print(min(candidates))
