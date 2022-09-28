import sys
from collections import deque
input = sys.stdin.readline

def bfs(x1,y1,x2,y2):
    que = deque()
    que.append((x1,y1))
    field[x1][y1] = 1
    while que:
        x,y = que.popleft()
        if x == x2 and y == y2:
            return field[x][y]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if field[nx][ny] == 0:
                field[nx][ny] = field[x][y]+1
                que.append((nx,ny))
T = int(input())
dx = [2,2,-2,-2,1,1,-1,-1]
dy = [1,-1,1,-1,2,-2,2,-2]

for _ in range(T):
    N = int(input())
    field = [[0]*N for _ in range(N)]
    x1, y1 = map(int,input().split())
    x2, y2 = map(int,input().split())
    print(bfs(x1,y1,x2,y2)-1)
