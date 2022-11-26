from sys import stdin; input=stdin.readline
from collections import deque
N, M = map(int,input().split())

needs = [0]*(N+1)
dt = {i:[] for i in range(1,N+1)}

for _ in range(M):
    a, b = map(int,input().split())
    dt[a].append(b)
    needs[b] += 1

que = deque()

for i in range(1,N+1):
    if needs[i] == 0:
        que.append(i)

while que:
    x = que.popleft()
    print(x, end=' ')
    for i in dt[x]:
        needs[i] -= 1
        if needs[i] == 0:
            que.append(i)

