from collections import deque

def bfs_w(x,y):
    que = deque()
    c = 1
    que.append((x,y))
    field[x][y] = 0
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if field[nx][ny] == 'W':
                c += 1
                field[nx][ny] = 0
                que.append((nx,ny))
    return c*c

def bfs_b(x,y):
    que = deque()
    c = 1
    que.append((x,y))
    field[x][y] = 0
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if field[nx][ny] == 'B':
                c += 1
                field[nx][ny] = 0
                que.append((nx,ny))
    return c*c
                

dx = [0,0,-1,1]
dy = [-1,1,0,0]

M, N = map(int,input().split())

field = [list(input()) for _ in range(N)]
W_cnt = 0
B_cnt = 0
for i in range(N):
    for j in range(M):
        if field[i][j] == 'W':
            W_cnt += bfs_w(i,j)
        elif field[i][j] == 'B':
            B_cnt += bfs_b(i,j)
print(W_cnt, B_cnt)