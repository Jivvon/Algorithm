"""
실패 (틀렸습니다)
"""
import sys


def near_info(arr, x, y, friends):
    count, empty = 0, 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[ny][nx] in friends:
                count += 1
            elif arr[ny][nx] == 0:
                empty += 1
    return count, empty


def find_position(arr: list, friends: list) -> (int, int):
    """
    1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
    """
    ranks = []  # count, empty, x, y

    for j in range(n):
        for i in range(n):
            if arr[j][i] == 0:
                count, empty = near_info(arr, i, j, friends)
                ranks.append([count, empty, i, j])
    ranks.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    _, _, x, y = ranks[0]

    return y, x


def solution(arr, _favor_students, _n):
    for k, v in _favor_students.items():
        y, x = find_position(arr, v)
        arr[y][x] = k

    # 점수
    scores = [1, 1, 10, 100, 1000]
    answer = 0
    for j in range(_n):
        for i in range(_n):
            count, _ = near_info(arr, i, j, _favor_students[arr[j][i]])
            answer += scores[count]

    print(answer)
    return answer


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    favor_students = dict()
    for _ in range(n ** 2):
        tmp = list(map(int, sys.stdin.readline().rstrip().split()))
        favor_students[tmp[0]] = tmp[1:]
    classroom = [[0] * n for _ in range(n)]
    solution(classroom, favor_students, n)
