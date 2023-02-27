# 마지막까지 갔을 경우, '갈 수 있었던 경로'에 값을 표시
# 0,0에서 분기시킨 루트들이 다 돌아오면, 루트 값만큼 수가 더해지게 됨

from sys import stdin; input = stdin.readline

def DFS(x,y):

    if x == N-1 and y == M-1: # 마지막까지 도착했을 시
        return 1 # 가능한 경로이기 때문에 1을 더해줌
    if visited[x][y] != -1: # 방문처리되었을 경우
        return visited[x][y] # 현재 방문값을 리턴
    visited[x][y] = 0 # 방문처리하고, DFS 분기 실행
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            continue
        if field[nx][ny] < field[x][y]: # 높이가 더 낮을 경우만 확인하기
            visited[x][y] += DFS(nx, ny) # 분기되었던 값을 더해주기 (끝에 도달했을 경우, 경로에 값이 추가)
    return visited[x][y] # 최종적으로 모인 경로의 수 반환하기

N, M = map(int,input().split())
dx = (1,0,-1,0)
dy = (0,1,0,-1)

field = [tuple(map(int,input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
print(DFS(0, 0))

