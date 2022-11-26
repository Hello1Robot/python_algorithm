from collections import deque
from sys import stdin; input=stdin.readline
def BFS(x=0, y=0):
    que = deque()
    visited[0][0] = field[0][0]
    que.append((x,y))
    while que:
        x,y = que.popleft()
        for dx, dy in [(0,1),(0,-1),(-1,0),(1,0)]:
            nx = x + dx
            ny = y + dy
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if visited[nx][ny] > field[nx][ny]+visited[x][y]:
                visited[nx][ny] = field[nx][ny]+visited[x][y]
                que.append((nx,ny))

t = 1
while True:
    
    N = int(input())
    if N == 0:
        break
    field = [tuple(map(int,input().split())) for _ in range(N)]
    visited = [[1e9]*N for _ in range(N)]
    BFS()

    print(f'Problem {t}: {visited[N-1][N-1]}')
    t += 1