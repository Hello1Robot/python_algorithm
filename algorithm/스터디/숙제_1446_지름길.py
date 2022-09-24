import sys
import heapq
input = sys.stdin.readline

# 다이나믹 프로그래밍과 더 가깝지않나?
# Back이 없기 때문에 다익스트라이기도 할 듯
# 현실의 도로문제를 해결하는 것
# x, y, c 라고 한다면
# y-x >= c 인 경우 아예 무시해도 됨(지름길아님)


INF = 10000000000 # 최대값 초기화
N, D = map(int,input().split()) # 지름길의 갯수, 고속도로
field = [[] for _ in range(D+1)] # D만큼 필드 생성하기
for i in range(D):
    field[i].append((i+1,1))
for _ in range(N):
    샛길 = list(map(int,input().split())) # 시작점, 끝점, 비용 순으로 들어옴
    if 샛길[1] - 샛길[0] >= 샛길[2]: # 지름길 아닌 지름길 제외
        continue
    if 샛길[1] > D: # 길초과지름길 제외
        continue
    field[샛길[0]].append((샛길[1], 샛길[2]))
distance = [INF]*(D+1)
distance[0] = 0

que = []
heapq.heappush(que, (0, 0))
while que:
    d, now = heapq.heappop(que)
    if distance[now] < d: continue

    for x in field[now]:
        cost = d + x[1]

        if distance[x[0]] > cost:
            distance[x[0]] = cost
            heapq.heappush(que, (cost, x[0]))

print(distance[D])
        

