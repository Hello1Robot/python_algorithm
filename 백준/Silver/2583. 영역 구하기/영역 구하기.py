from collections import deque
def bfs(x,y):
    que = deque()
    que.append((x,y))
    field[x][y] = 0
    cnt = 1
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if field[nx][ny] == 1:
                cnt += 1
                field[nx][ny] = 0
                que.append((nx,ny))
    return cnt
        

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
N, M, K = map(int,input().split())

field = [[1]*M for _ in range(N)]
res_list = []
for _ in range(K):
    y1, x1, y2, x2 = map(int,input().split()) # 1 1 2 5
    for i in range(x1, x2):
        for j in range(y1, y2):
            field[i][j] = 0
for i in range(N):
    for j in range(M):
        if field[i][j] == 1:
            res_list.append(bfs(i,j))

res_list.sort()
print(len(res_list))
print(*res_list)
    