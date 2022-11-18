from sys import stdin; input=stdin.readline
from collections import deque
N = int(input())
needto = [0]*(N+1)
next = {i:[] for i in range(1,N+1)}
cost = [0]*(N+1)
tot_cost = [0]*(N+1)
que = deque()
for i in range(1,N+1):
    c, x, *n = map(int,input().split())
    cost[i] = c
    needto[i] = x
    if x == 0:
        que.append(i)
        tot_cost[i] = c
        continue
    for m in n:
        next[m].append(i)



while que:
    x = que.popleft()
    cst = tot_cost[x]
    for j in next[x]:
        tot_cost[j] = max(tot_cost[j], cst+cost[j])
        needto[j] -= 1
        if needto[j] == 0:
            que.append(j)

print(max(tot_cost))
