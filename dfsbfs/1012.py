from collections import deque
import sys

# 좌 상 우 하
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        arr[x][y] = 0 # 다시 검색하지 않게
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if arr[nx][ny] == 1:
                queue.append((nx, ny))
                arr[nx][ny] = 0 # 얘가 있어야 메모리 초과가 안 뜬다
                # 탐색을 했으면 반드시 다시 가지 않도록 해야한다.
                # queue는 탐색을 한 배추가 있는 저장소.

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        M, N, K = list(map(int, sys.stdin.readline().split())) # 가로, 세로, 배추 개수
        arr = [[0 for ___ in range(N)] for __ in range(M)]
        cnt = 0 # 맵에 있는 연결되어 있는 배추 묶음
        for __ in range(K): # 맵 그리기
            x, y = map(int, sys.stdin.readline().split())
            arr[x][y] = 1 # 맵에 배추 넣기
        for i in range(M):
            for j in range(N):
                if arr[i][j] == 1:
                    bfs((i,j))
                    cnt += 1
        print(cnt)
