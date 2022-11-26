# k만큼 벽부수기 가능
from collections import deque
from sys import stdin
input = stdin.readline

def bfs():
    que = deque()
    que.append((0,0,0))
    visited[0][0][0] = 1
    while que:
        x,y,w = que.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nw = w + 1
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if visited[nx][ny][w]:
                continue
            if w < K and field[nx][ny] == '1':
                visited[nx][ny][nw] = visited[x][y][w] + 1
                que.append((nx,ny,nw))
                continue
            if field[nx][ny] == '0':
                visited[nx][ny][w] = visited[x][y][w] + 1
                que.append((nx,ny,w))
                

    return -1
    
dx = (-1,0,1,0)
dy = (0,1,0,-1)
N, M, K = map(int,input().split())
field = [list(input()) for _ in range(N)]
visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
# visited = [[[0 * M] for _ in range(N)] for _ in range(K+1)]
print(bfs())
