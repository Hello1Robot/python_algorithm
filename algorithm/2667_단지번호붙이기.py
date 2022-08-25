from collections import deque

def bfs(x,y):
    cnt = 1
    que = deque()
    que.append((x,y))
    field[x][y] = 0
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and field[nx][ny] == 1:
                field[nx][ny] = 0
                cnt += 1
                que.append((nx,ny))
    return cnt



dx = [0,0,-1,1]
dy = [-1,1,0,0]

# bfs 사용하기

N = int(input())
field = [list(map(int,input())) for _ in range(N)]
bfs_list = []
res = []
for i in range(N):
    for j in range(N):
        if field[i][j] == 1:
            res.append(bfs(i,j))

res.sort()
print(len(res))
for danji in res:
    print(danji)