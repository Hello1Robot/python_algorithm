import sys
input = sys.stdin.readline
from collections import deque
def BFS(start):
    que = deque()
    visited[start] = 1
    que.append(start)
    while que:
        x = que.popleft()
        for i in nodes[x]:
            if not visited[i]:
                que.append(i)
                visited[i] = visited[x] + 1
    for i in range(1,N+1):
        if visited[i] == K+1:
            res_list.append(i)
            

N, M, K, START = map(int,input().split())

nodes = {i:[] for i in range(1,N+1)}
for _ in range(M):
    start, end = map(int,input().split())
    nodes[start].append(end)

visited = [0]*(N+1)
res_list = []
BFS(START)

if res_list:
    for res in res_list:
        print(res)
else:
    print(-1)
