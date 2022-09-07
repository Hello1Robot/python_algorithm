import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    visited = [0]*(N+1)
    que = deque()
    que.append((x,y))
    while que:
        x,y = que.popleft()
        

dx = [1,0,-1,0]
dy = [0,-1,0,1]
N, M = map(int,input().split()) # N은 노드의 수, M은 연결관계의 수
field = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    field[a][b] = 1
    field[b][a] = 1

