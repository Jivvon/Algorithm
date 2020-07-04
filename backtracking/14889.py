import sys, itertools
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

answer = 999999
teams = itertools.combinations(range(N), N//2) # 가능한 팀의 조합
teams = filter(lambda x:0 in x,teams) # 모든 가능한 팀의 조합의 절반 (0번째 선수를 포함하는 조합)

for team in teams:
    team_A = set(team)
    team_B = set(range(N))-set(team)
    team_A_score = 0
    team_B_score = 0
    for (i, j) in itertools.permutations(team_A, 2):
        team_A_score += arr[i][j]
    for (i, j) in itertools.permutations(team_B, 2):
        team_B_score += arr[i][j]
    answer = min(answer, abs(team_A_score-team_B_score))

print(answer)
