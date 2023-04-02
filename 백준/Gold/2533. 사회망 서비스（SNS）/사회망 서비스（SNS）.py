from sys import stdin; input=stdin.readline
from collections import defaultdict

N = int(input())

nodes = defaultdict(list)
# visited = [0]*(N+1)
conn = [0]*(N+1)
leafs = []
res = 0
for _ in range(N-1): # 간선 갯수 N-1개
    stt, end = map(int,input().split())
    nodes[stt].append(end)
    nodes[end].append(stt)
    conn[stt] += 1
    conn[end] += 1



for i in range(1,N+1):
    if conn[i] == 1:
        leafs.append(i)

while leafs:
    x = leafs.pop()
    for i in nodes[x]:
        for j in nodes[i]:
            nodes[j].remove(i)
            if len(nodes[j]) == 1:
                leafs.append(j)
        # visited[i] = 1
        res += 1
        nodes[i].clear()
print(res)
