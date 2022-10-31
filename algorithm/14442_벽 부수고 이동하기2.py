# k만큼 벽부수기 가능

from collections import deque

def 벽하나부수기(x,y,w):
    que = deque()
    que.append((x,y,w))
    visited[x][y][w] = 1
    while que:
        x,y,w = que.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if w < K and field[nx][ny] == '1' and visited[nx][ny][w] == 0:
                visited[nx][ny][w+1] = visited[x][y][w] + 1
                que.append((nx,ny,w+1))
            elif field[nx][ny] == '0' and visited[nx][ny][w] == 0:
                visited[nx][ny][w] = visited[x][y][w] + 1
                que.append((nx,ny,w))
    return -1
    
dx = [1,-1,0,0]
dy = [0,0,1,-1]
N, M, K = map(int,input().split())
field = [list(input()) for _ in range(N)]
visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
print(벽하나부수기(0,0,0))
