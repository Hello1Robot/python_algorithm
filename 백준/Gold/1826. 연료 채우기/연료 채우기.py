from sys import stdin; input = stdin.readline
import heapq

N = int(input())
que = []
for _ in range(N+1):
    dis, fuel = map(int,input().split())
    que.append((dis, fuel))

energy = que[N][1]
que.sort()


now = 0
cnt = 0
hq = []

for i in range(N+1):
    dis = que[i][0] - now
    now = que[i][0]
    if dis > energy:
        while dis > energy:
            if hq:
                energy -= heapq.heappop(hq)
                cnt += 1
            else:
                print(-1)
                exit()

    energy -= dis
    heapq.heappush(hq, -que[i][1])

print(cnt)