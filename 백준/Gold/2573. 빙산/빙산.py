from sys import stdin; input = stdin.readline
from collections import deque
# 매 해 동시에 없어지기 때문에
# 하나를 돌 때마다 직접적으로 리스트를 건들면
# 곤란곤란
# 다 돌고 나서 처리해야 함

def BFS(x, y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    seas = []

    while q:
        x, y = q.popleft()
        sea = 0
        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx = x + dx
            ny = y + dy
            
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue

            if not field[nx][ny]:
                sea += 1
            elif field[nx][ny] and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = 1
        
        if sea > 0:
            seas.append((x, y, sea))
    
    for x, y, sea in seas:
        field[x][y] = max(0, field[x][y] - sea)
    
    return 1
                


N, M = map(int,input().split())
field = [list(map(int,input().split())) for _ in range(N)]
res = 0
cnt = 0
que = []
for i in range(N):
    for j in range(M):
        if field[i][j]:
            que.append((i, j))

while que:
    visited = [[0]*M for _ in range(N)]
    melt = []
    pieces = 0
    for x, y in que:
        if field[x][y] and not visited[x][y]:
            pieces += BFS(x,y)
        if field[x][y] == 0:
            melt.append((x,y))
    if pieces > 1:
        res = cnt
        break

    que = list(set(que) - set(melt))

    cnt += 1

print(res)