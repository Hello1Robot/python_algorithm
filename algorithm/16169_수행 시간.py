from collections import deque
from sys import stdin; input = stdin.readline
N = int(input())
que = deque()
needs = [0]*(N+1)
visited = [0]*(N+1)
costs = [0] * (N+1)
tot_cost = [0] * (N+1)
for i in range(1,N+1):
    계급, 동작속도 = map(int,input().split())
    needs[i] = 계급-1
    costs[i] = 동작속도
    if 계급 == 1:
        que.append(i)
        tot_cost[i] = 동작속도

while que:
    x = que.popleft()
    now = tot_cost[x]
    visited[x] = 1
    for j in range(1,N+1):
        if not visited[j]:
            tot_cost[j] = max(tot_cost[j], now+costs[j])
            needs[j] -= 1
            if needs[j] == 0:
                que.append(j)

max_res = 0
for z in range(1,N+1):
    max_res = max(max_res, tot_cost[z])

print(max_res)
