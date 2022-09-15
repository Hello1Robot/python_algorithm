import sys
import heapq
input = sys.stdin.readline


def 데이크스트라인지뭔지(start):
    que = []
    que.append((0,start))
    distance[start] = 0
    while que:
        dis, now = heapq.heappop(que)
        if distance[now] < dis:
            continue
        for node, cost in nodes[now]:
            cost = cost + dis
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(que, (cost, node))
        


INF = 3000000
V, E = map(int,input().split())
nodes = [[] for _ in range(V+1)]
distance = [INF]*(V+1)
start = int(input())
for _ in range(E):
    a, b, c = map(int,input().split())
    nodes[a].append((b,c))

데이크스트라인지뭔지(start)
for i in range(1,V+1):
    if distance[i] >= INF:
        print('INF')
    else:
        print(distance[i])