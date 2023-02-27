from sys import stdin; input=stdin.readline
from collections import deque
def BFS(x=1):
    que = deque()
    parent[x] = -1
    que.append(x)
    while que:
        x = que.popleft()
        for i in nodes[x]:
            if not parent[i]:
                parent[i] = x
                que.append(i)
                


N = int(input())
nodes = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)

parent = [0] * (N+1)

BFS()
for j in range(2,N+1):
    print(parent[j])