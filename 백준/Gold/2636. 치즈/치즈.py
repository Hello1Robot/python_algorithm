
from sys import stdin; input=stdin.readline

from collections import deque

N, M = map(int,input().split())

field = [list(map(int,input().split())) for _ in range(N)]

time = 0

cheese = 0

for i in range(N):

    for j in range(M):

        if field[i][j] == 1:

            cheese += 1

while cheese:

    time += 1

    visited = [[0]*M for _ in range(N)]

    que = deque()

    que.append((0,0))

    visited[0][0] = 1

    cnt = 0

    while que:

        x, y = que.popleft()

        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:

            nx, ny = x + dx, y + dy

            

            if nx >= N or nx < 0 or ny >= M or ny < 0 or visited[nx][ny] == 1:

                continue

            

            if field[nx][ny] == 0:

                visited[nx][ny] = 1

                que.append((nx,ny))

            else:

                field[nx][ny] = 0

                visited[nx][ny] = 1

                cnt += 1

    

    cheese -= cnt

print(time)

print(cnt)
