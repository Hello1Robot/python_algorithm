from sys import stdin; input = stdin.readline
from collections import deque

N, M = map(int,input().split())
needs = [0]*(N+1)
nexts = {i:[] for i in range(1,N+1)}
que = deque()
res = []
for _ in range(M):
    a, *rst = map(int,input().split())
    for x in range(a):
        needs[rst[x]] += x
        if a == x+1:
            continue
        nexts[rst[x]] += rst[x+1:]
for i in range(1,N+1):
    if needs[i] == 0:
        que.append(i)

while que:
    start = que.popleft()
    res.append(start)
    for next in nexts[start]:
        needs[next] -= 1
        if needs[next] == 0:
            que.append(next)

if sum(needs) != 0:
    print(0)
else:
    for r in res:
        print(r)

