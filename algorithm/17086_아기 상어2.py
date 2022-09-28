from collections import deque


N, M = map(int,input().split())
dx = [0,0,-1,1,-1,-1,1,1]
dy = [-1,1,0,0,1,-1,1,-1]
field = [list(map(int,input().split())) for _ in range(N)]
max_cnt = 0
que = deque()
for i in range(N):
    for j in range(M):
        if field[i][j] == 1:
            que.append((i,j))

while que:
    x,y = que.popleft()
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            continue
        if field[nx][ny] == 0:
            field[nx][ny] = field[x][y] + 1
            que.append((nx,ny))

for i in range(N):
    for j in range(M):
        if field[i][j] > max_cnt:
            max_cnt = field[i][j]

print(max_cnt-1)