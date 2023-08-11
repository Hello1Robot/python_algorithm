# 벽부수기인데 카운트 제일 적게 해야 하니까
# 가능한 것들 중 덜부순친구가 제일 먼저 가도록 하고
# heapq를 통해서 해결
import heapq
from sys import stdin; input=stdin.readline

N, M = map(int,input().split())

field = [list(input().rstrip()) for _ in range(M)]
que = []
heapq.heappush(que, (0,0,0))
dr = [(0,1),(1,0),(-1,0),(0,-1)]
visited = [[0]*N for _ in range(M)]
visited[0][0] = 1
while que:
    cnt, x, y = heapq.heappop(que)
    if y == N-1 and x == M-1:
        print(cnt)
        break
    
    for dx, dy in dr:
        nx = x + dx
        ny = y + dy

        if nx >= M or nx < 0 or ny >= N or ny < 0:
            continue

        if visited[nx][ny]:
            continue

        if field[nx][ny] == '1':
            heapq.heappush(que, (cnt+1, nx,ny))
        
        else:
            heapq.heappush(que, (cnt, nx, ny))
        
        visited[nx][ny] = 1
