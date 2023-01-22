import sys
input = sys.stdin.readline

def DFS(x,y):
    global cnt
    if x == N-1 and y == M-1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            continue
        if field[nx][ny] < field[x][y]:
            visited[x][y] += DFS(nx, ny)
    return visited[x][y]

N, M = map(int,input().split())
dx = (1,0,-1,0)
dy = (0,1,0,-1)

field = [tuple(map(int,input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
print(DFS(0, 0))

