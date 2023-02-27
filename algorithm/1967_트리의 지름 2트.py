# DFS로 재귀돌리기
from sys import stdin; input=stdin.readline
from collections import defaultdict

def DFS(x):
    global max_val
    global max_idx
    if visited[x] > max_val:
        max_val = visited[x]
        max_idx = x
    for i, v in nodes[x]:
        if visited[i] == -1:
            visited[i] = visited[x] + v
            DFS(i)
    

N = int(input())
mx1 = 0
mx2 = 0
nodes = [[] for _ in range(N+1)]
for _ in range(N-1):
    pa, son, val = map(int,input().split())
    nodes[pa].append((son, val))
    nodes[son].append((pa, val))

visited = [-1]*(N+1)
max_val, max_idx = 0, -1
visited[1] = 0




