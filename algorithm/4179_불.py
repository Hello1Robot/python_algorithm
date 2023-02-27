from collections import deque

N, M = map(int,input().split())

field = [list(input()) for _ in range(N)]
bul_cnt = 0
que = deque()
visited = [[0]*M for _ in range(N)]
cnt = 2
sx, sy = -1, -1


for i in range(N):
    for j in range(M):
        if field[i][j] == 'J':
            if i == 0 or i == N-1 or j == 0 or j == M-1:
                print(1)
                exit()
            sx, sy = i, j
                
        if field[i][j] == 'F':
            que.append((1,i,j))

visited[sx][sy] = 1

for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
    nx = sx + dx
    ny = sx + dy
    if nx >= N or nx < 0 or ny >= M or ny < 0 or field[nx][ny] != '.' or visited[nx][ny]:
        continue
    
    visited[nx][ny] = 1
    que.append((0, nx, ny))

while que:
    tp, x, y = que.popleft()

    if tp == 0 and (x == 0 or x == N-1 or y == 0 or y == M-1):
        print(cnt)
        exit()
    
    for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
        nx = x + dx
        ny = x + dy
        
        if tp == 0:
            if nx >= N or nx < 0 or ny >= M or ny < 0 or field[nx][ny] != '.' or visited[nx][ny]:
                continue
            cnt += 1
            visited[nx][ny] = 1
            que.append((tp, nx, ny))
        
        else:
            if nx >= N or nx < 0 or ny >= M or ny < 0 or field[nx][ny] == '#' or field[nx][ny] == 'F' or visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            field[nx][ny] = 'F'
            que.append((tp,nx,ny))

print('IMPOSSIBLE')