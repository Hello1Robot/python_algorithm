import sys
input = sys.stdin.readline

# 다이나믹 프로그래밍과 더 가깝지않나?
# Back이 없기 때문에 다익스트라이기도 할 듯
# 현실의 도로문제를 해결하는 것
# x, y, c 라고 한다면
# y-x >= c 인 경우 아예 무시해도 됨(지름길아님)
# 이외의 경우에 대해서 DP테이블을 이중으로 만들고
# 각자 실행하여 최저비용을 선정한다.

INF = 10000000000 # 최대값 초기화
샛길들 = []
N, D = map(int,input().split())
for _ in range(N):
    샛길 = list(map(int,input().split())) # 시작점, 끝점, 비용 순으로 들어옴
    if 샛길[1] - 샛길[0] >= 샛길[2]:
        continue
    샛길들.append(샛길)
N = len(샛길들)
샛길들.sort()
DP = [[INF]*(D+1) for _ in range(N)]
for i in range(N):
    start, end, cost = 샛길들[i]

