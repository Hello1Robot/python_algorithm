from sys import stdin; input=stdin.readline
from collections import deque

N = int(input())
num_dict = {i:[] for i in range(1,N+1)}
costs = [0]*(N+1)
needs = [0]*(N+1)
tot_time = [0]*(N+1)
que = deque()
for i in range(1,N+1):
    cost, *nodes = map(int,input().split())
    costs[i] = cost
    for x in nodes:
        if x == -1:
            break
        else:
            num_dict[i].append(x)
            needs[x] += 1
for i in range(1,N+1):
    if needs[i] == 0:
        que.append(i)
        tot_time[i] = costs[i]

while que:
    x = que.popleft()
    cost = costs[x]
    for y in num_dict[x]:
        tot_time[y] = max(tot_time[y], cost+costs[y])
        needs[y] -= 1
        if needs[y] == 0:
            que.append(y)
print(num_dict)
for i in range(1,N+1):
    print(tot_time[i])