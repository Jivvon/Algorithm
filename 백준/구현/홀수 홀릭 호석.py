import sys
from collections import deque

n = sys.stdin.readline().rstrip()


def odds_total(num: str):
    return sum(map(lambda x: int(x) % 2, list(num)))


def sum_num_list(nums: list) -> str:
    return str(sum(map(int, nums)))


answers = []
q = deque()  # [num:str, odd_cnt]
q.append([n, odds_total(n)])
while q:
    num, odd_cnt = q.popleft()
    _len = len(num)
    if _len == 1:
        answers.append(odd_cnt)
        continue
    elif _len == 2:
        cur_nums = str(sum_num_list(num))
        cur_total = odds_total(cur_nums)
        q.append([cur_nums, odd_cnt + cur_total])
    elif _len >= 3:
        for i in range(1, _len):
            for j in range(i + 1, _len):
                a, b, c = num[:i], num[i:j], num[j:]
                cur_nums = str(sum_num_list([a, b, c]))
                cur_total = odds_total(cur_nums)
                q.append([cur_nums, odd_cnt + cur_total])

print(min(answers), max(answers))
