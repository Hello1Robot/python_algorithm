# k만큼 벽부수기 가능
from collections import deque
from sys import stdin
input = stdin.readline

def 벽여러개부수기(x,y,w):
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

            # if nx >= N or nx < 0 or ny >= M or ny < 0:
            #     continue
            if nx < N and nx >= 0 and ny < M and ny >= 0 and visited[nx][ny][w] == 0:

                if field[nx][ny] == '0':
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    que.append((nx,ny,w))

                elif w < K and field[nx][ny] == '1':
                    visited[nx][ny][w+1] = visited[x][y][w] + 1
                    que.append((nx,ny,w+1))
    return -1
    
dx = [1,0,0,-1]
dy = [0,1,-1,0]
N, M, K = map(int,input().split())
field = [tuple(input()) for _ in range(N)]
visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
# visited = [[[0 * M] for _ in range(N)] for _ in range(K+1)]
print(벽여러개부수기(0,0,0))
