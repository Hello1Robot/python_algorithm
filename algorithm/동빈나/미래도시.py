# 굳이 10억으로 초기화를 해야할지는 모르겠다
INF = int(1e9)

# 노드의 개수 및 간선의 개수 입력받기
N, M = map(int,input().split())
# 2차원 그래프를 만들고 전부 INF로 초기화
graph = [[INF]*(N+1) for _ in range(N+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    # A와 B 사이의 양방향 그래프
    # 각 이동비요은 1
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 목표 노드 x와 최종 목적지 k 입력받기
x, k = map(int,input().split())

# 플로이드 워셜 알고리즘 수행
for k in range(1, N+1): # 경유지
    for a in range(1, N+1):
        for b in range(1, N+1):
            # 그냥 a에서 b로 가는 것과 a에서 k를 경유해서 b로 가는 것 비교
            # 만약 가지 못할경우 값이 무한대이므로 넘어갈 것
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)