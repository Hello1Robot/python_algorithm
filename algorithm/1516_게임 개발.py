from sys import stdin; input = stdin.readline
from collections import deque
N = int(input())

needto = [0]*(N+1)
next = {i:[] for i in range(1,N+1)}
cost = [0]*(N+1)
tot_cost = [0]*(N+1)
que = deque()
for i in range(1,N+1):
    cst, *pre = map(int,input().split())
    cost[i] = cst
    for p in pre:
        if p == -1:
            break
        next[p].append(i)
        needto[i] += 1
    if needto[i] == 0:
        que.append(i)
        tot_cost[i] = cost[i]

while que:
    x = que.popleft()
    cst = tot_cost[x]
    for nx in next[x]:
        tot_cost[nx] = max(tot_cost[nx], cost[nx]+cst)
        needto[nx] -= 1
        if needto[nx] == 0:
            que.append(nx)

for i in range(1,N+1):
    print(tot_cost[i])
