def DFS(x=0,y=0):
    global cnt
    if x == N-1 and y == M-1:
        cnt += 1
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            continue
        if field[nx][ny] < field[x][y]:
            visited[nx][ny] = 1
            DFS(nx,ny)
            visited[nx][ny] = 0

N, M = map(int,input().split())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
cnt = 0
field = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
DFS()
print(cnt)
