from collections import deque
from copy import deepcopy

def red_BFS(x,y,field):
    que = deque()
    que.append((x,y))
    field[x][y] = 0
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if field[nx][ny] == 'R':
                que.append((nx,ny))
                field[nx][ny] = 0

def blue_BFS(x,y,field):
    que = deque()
    que.append((x,y))
    field[x][y] = 0
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if field[nx][ny] == 'B':
                que.append((nx,ny))
                field[nx][ny] = 0

def green_BFS(x,y,field):
    que = deque()
    que.append((x,y))
    field[x][y] = 0
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if field[nx][ny] == 'G':
                que.append((nx,ny))
                field[nx][ny] = 0

def rg_BFS(x,y,field):
    que = deque()
    que.append((x,y))
    field[x][y] = 0
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if field[nx][ny] == 'G' or field[nx][ny] == 'R':
                que.append((nx,ny))
                field[nx][ny] = 0

dx = [0,1,0,-1]
dy = [-1,0,1,0]
N = int(input())
origin_field = [list(input()) for _ in range(N)]
rgb_field = deepcopy(origin_field)
cnt = 0
rg_cnt = 0
for i in range(N):
    for j in range(N):
        if origin_field[i][j] == 'R':
            cnt += 1
            red_BFS(i,j,origin_field)
        elif origin_field[i][j] == 'B':
            cnt += 1
            blue_BFS(i,j,origin_field)
        elif origin_field[i][j] == 'G':
            cnt += 1
            green_BFS(i,j,origin_field)
        else:
            continue

for i in range(N):
    for j in range(N):
        if rgb_field[i][j] == 'R' or rgb_field[i][j] == 'G':
            rg_cnt += 1
            rg_BFS(i,j,rgb_field)
        elif rgb_field[i][j] == 'B':
            rg_cnt += 1
            blue_BFS(i,j,rgb_field)
        else:
            continue

print(f'{cnt} {rg_cnt}')