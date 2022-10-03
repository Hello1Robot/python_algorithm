import sys
import heapq
input = sys.stdin.readline

def 다익스트라(start,distance):
    que= []
    # 시작 노드는 거리 0
    heapq.heappush(que, (0,start))
    distance[start] = 0
    while que:
        # 최단거리 정보 꺼내기
        dis, now = heapq.heappop(que)
        # 방문한 노드면 무시
        if distance[now] < dis:
            continue # visited와 동일한 역할
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for node, cst in field[now]:
            cost = dis + cst
            # 기존 거리보다 짧은 경우
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(que, (cost, node))


INF = 1e9
N, M = map(int,input().split())
field = [[] for i in range(N+1)]

for _ in range(M):
    a, b, c = map(int,input().split())
    field[a].append((b,c))
    field[b].append((a,c))
dis1 = [INF] * (N+1)
disx = [INF] * (N+1)
disy = [INF] * (N+1)


x,y = map(int,input().split())
다익스트라(1, dis1)
다익스트라(x, disx)
다익스트라(y, disy)
dist = min(dis1[x]+disx[y]+disy[N], dis1[y]+disy[x]+disx[N])
if dist >= INF:
    print(-1)
else:
    print(dist)