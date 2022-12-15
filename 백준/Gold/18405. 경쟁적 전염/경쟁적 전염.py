from collections import deque
from sys import stdin; input=stdin.readline

N, K = map(int,input().split())
field = [list(map(int,input().split())) for _ in range(N)]
que = []
for i in range(N):
    for j in range(N):
        if field[i][j]:
            que.append((field[i][j], i, j, 0))

que.sort()
q = deque(que)

sec, ex, ey = map(int,input().split())
while q:
    typ, x, y, cnt = q.popleft()
    if cnt == sec:
        break
    
    for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        nx, ny = x + dx, y + dy

        if nx >= N or ny >= N or nx < 0 or ny < 0 or field[nx][ny]:
            continue
        field[nx][ny] = typ
        q.append((typ, nx, ny, cnt+1))

print(field[ex-1][ey-1])
    