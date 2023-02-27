# 힙큐 써서 풀어보자
from sys import stdin; input = stdin.readline
import heapq

N = int(input())

field = [tuple(input().strip()) for _ in range(N)]
visited = [[1e9]*N for _ in range(N)]
que = []
if field[0][0] == '0':
    que.append((1,0,0))
    visited[0][0] = 1
else:
    que.append((0,0,0))
    visited[0][0] = 0


while que:

    crush, x, y = heapq.heappop(que)

    if x == N-1 and y == N-1:
        print(crush)
        break

    for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
        nx, ny = x + dx, y + dy
        
        if nx >= N or nx < 0 or ny >= N or ny < 0:
            continue
        
        if field[nx][ny] == '1':
            if crush < visited[nx][ny]:
                visited[nx][ny] = crush
                heapq.heappush(que, (crush, nx, ny))

        else:
            if crush + 1 < visited[nx][ny]:
                visited[nx][ny] = crush+1
                heapq.heappush(que, (crush+1, nx, ny))
