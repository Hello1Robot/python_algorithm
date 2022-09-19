import sys
import heapq
input = sys.stdin.readline

def 다익스트라(start):
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

INF = 1000000000
N = int(input()) # 도시의 개수 입력받기
M = int(input()) # 간선의 개수 입력받기
field = [[] for i in range(N+1)]
distance = [INF] * (N+1)
for _ in range(M):
    a, b, c = map(int,input().split())
    field[a].append((b,c))

start, end = map(int,input().split())
다익스트라(start)
print(distance[end])
