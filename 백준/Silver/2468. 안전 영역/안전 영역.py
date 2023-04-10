from sys import stdin; input=stdin.readline
from collections import deque
def BFS(x,y):
    que = deque()
    que.append((x,y))
    
    while que:
        a, b = que.popleft()
        
        for dx, dy in delta:
            nx, ny = a + dx, b + dy
            if nx >= N or nx < 0 or ny >= N or ny < 0 or not field[nx][ny] or visited[nx][ny]:
                continue
            field[nx][ny] -= 1
            visited[nx][ny] = 1
            que.append((nx,ny))

    return 1
        

N = int(input())
delta = [(0,1),(1,0),(0,-1),(-1,0)]
field = [list(map(int,input().split())) for _ in range(N)]
res = 1
max_val = 0
for i in range(N):
    for j in range(N):
        max_val = max(max_val, field[i][j])
for _ in range(max_val):
    visited = [[0]*N for _ in range(N)]
    now = 0
    for i in range(N):
        for j in range(N):
            if field[i][j] and not visited[i][j]:
                field[i][j] -= 1
                visited[i][j] = 1
                now += BFS(i,j)
    res = max(now, res)

print(res)
    
