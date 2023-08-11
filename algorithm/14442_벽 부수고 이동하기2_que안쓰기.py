# k만큼 벽부수기 가능
from sys import stdin
input = stdin.readline

def bfs():
    que = []
    que.append((0,0,0))
    visited[0][0][0] = 1
    while que:
        new_que = []
        for x, y, w in que:
            if x == N-1 and y == M-1:
                return visited[w][x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                nw = w + 1
                if nx >= N or nx < 0 or ny >= M or ny < 0:
                    continue
                if visited[w][nx][ny]:
                    continue
                if field[nx][ny] == '0':
                    visited[w][nx][ny] = visited[w][x][y] + 1
                    new_que.append((nx,ny,w))
                elif field[nx][ny] == '1' and w < K :
                    visited[nw][nx][ny] = visited[w][x][y] + 1
                    new_que.append((nx,ny,nw))


        que = new_que
                

    return -1
    
dx = (-1,0,1,0)
dy = (0,1,0,-1)
N, M, K = map(int,input().split())
field = [list(input()) for _ in range(N)]
# visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
visited = [[[0 * M] for _ in range(N)] for _ in range(K+1)]
print(bfs())
