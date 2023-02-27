from sys import stdin; input=stdin.readline
from collections import defaultdict, deque

N, M = map(int,input().split())
level = [0]*(N+1)
needs = [0]*(N+1)
next = defaultdict(list)
que = deque()
for _ in range(M):
    pre, nex = map(int,input().split())
    needs[nex] += 1
    next[pre].append(nex)

for i in range(1,N+1):
    if needs[i] == 0:
        que.append(i)
        level[i] = 1

while que:
    x = que.popleft()
    
    for q in next[x]:
        needs[q] -= 1
        if needs[q] == 0:
            level[q] = level[x] + 1
            que.append(q)

for x in range(1,N+1):
    print(level[x], end=" ")