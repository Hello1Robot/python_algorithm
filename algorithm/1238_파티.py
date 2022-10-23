from sys import stdin
import heapq
input = stdin.readline

def 다익스트라(start):
    distance = [INF]*(N+1)
    que= []
    # 시작 노드는 거리 0
    heapq.heappush(que, (0,start))
    distance[start] = 0
    while que:
        # 최단거리 정보 꺼내기
        비용, 출발지 = heapq.heappop(que)
        # 방문한 노드면 무시
        if distance[출발지] < 비용:
            continue # visited와 동일한 역할
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for node, cst in field[출발지]:
            cost = 비용 + cst
            # 기존 거리보다 짧은 경우
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(que, (cost, node))
    if start == X:
        return distance[:]
    return distance[X]


INF = 1e9
N, M, X = map(int,input().split())
max_time = 0
field = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int,input().split())
    field[a].append((b, c))

disx = 다익스트라(X)

for x in range(1,N+1):
    if x == X:
        continue
    max_time = max(max_time, 다익스트라(x)+disx[x])

print(max_time)