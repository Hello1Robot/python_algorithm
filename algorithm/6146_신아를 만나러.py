from sys import stdin; input = stdin.readline
from collections import deque

def BFS(x=500, y=500):
    que = deque()
    que.append((x,y))
    field[x][y] = 0
    
    while que:
        x, y = que.popleft()
        if x == end_x and y == end_y:
            print(field[x][y])
            exit()
        
        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx, ny = x+dx, y+dy
            
            if nx > 1000 or nx < 0 or ny > 1000 or ny < 0:
                continue
            
            if field[nx][ny] == -2:
                field[nx][ny] = field[x][y] + 1
                que.append((nx,ny))
            
            
            
    



end_x, end_y, K = map(int,input().split())
end_x, end_y = end_x+500, end_y+500

field = [[-2]*1001 for _ in range(1001)]
for _ in range(K):
    x, y = map(int,input().split())
    field[x+500][y+500] = -1

BFS()