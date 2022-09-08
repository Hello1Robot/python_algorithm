import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    que = deque()
    que.append(x)
    visited[x] == 1
    while que:
        x = que.popleft()
        for i in range(1,N+1):
            if field[x][i] == 1 and visited[i] == 0:
                visited[i] = 1
                que.append(i)

N, M = map(int,input().split())
field = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 0
for i in range(M):
    a,b = map(int,input().split())
    field[a][b] = 1
    field[b][a] = 1

for j in range(1,N+1):
    if visited[j] == 0:
        bfs(j)
        cnt += 1

print(cnt)