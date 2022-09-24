from collections import deque

def bfs(x,y):
    visited = [[0]*M for _ in range(N)]
    que = deque()
    max_cnt = 0
    que.append((x,y))
    visited[x][y] = 1
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0 or visited[nx][ny] != 0 or field[nx][ny] == 'W':
                continue
            visited[nx][ny] = visited[x][y] + 1
            que.append((nx,ny))
    
    for i in range(N):
        for j in range(M):
            if visited[i][j] > max_cnt:
                max_cnt = visited[i][j]
    return max_cnt
            
            


N, M = map(int,input().split())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
res = 0
field = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if field[i][j] == 'L':
            cnt = bfs(i,j)
            if cnt > res:
                res = cnt

print(res-1)