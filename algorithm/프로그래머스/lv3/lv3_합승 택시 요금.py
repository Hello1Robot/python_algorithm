import sys
import heapq
input = sys.stdin.readline
def 다익스트라(start, end, n, field):
    que = []

    distance = [1000000000]*(n+1)
    heapq.heappush(que, (0,start))
    distance[start] = 0
    while que:
        dis, now = heapq.heappop(que)

        if now == end:
            
            return distance[end]
        if distance[now] < dis:
            continue
        for node, cst in field[now]:
            cost = dis + cst

            if cost < distance[node]:
                distance[node] = cost
                
                heapq.heappush(que, (cost, node))



def solution(n, s, a, b, fares):
    answer = 0
    field = [[] for i in range(n+1)]
    for fare in fares:
        stt, end, cost = fare
        field[stt].append((end,cost))
        field[end].append((stt,cost))
    A길 = 다익스트라(s,a,n, field)
    B길 = 다익스트라(s,b, n, field)
    AB사이 = 다익스트라(a,b, n, field)
    # print(f'A길:{A길}')
    # print(f'B길:{B길}')
    # print(f'AB사이:{AB사이}')
    A먼저 = AB사이 + A길
    B먼저 = AB사이 + B길
    따로따로 = A길 + B길
    answer = min(A먼저, B먼저, 따로따로)
    return answer




# 노드 수 : n
# 출발 지점 : s
# a의 도착점 : a
# b의 도착점 : b
# A에서 C로 가는 최단 거리 구함 - A에서 D로 가는 최단거리 구함 - A에서 C를 거쳐 D를 가는 비용 구함 - A에서 D를 거쳐 C로 가는 비용 구함 - 셋 비교
print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))

# 문제 이해를 좀 잘못한듯
# 이게 중간에 내려서 따로 택시타는 경우도 있어서
# 전체적인 값을 고려할 필요가 생겨버림...
# 그래서 어디가 가장 적절한 가운데지점인지 찾아볼 필요가 있음

# 다익스트라를 통해서 전체경로 최저비용 구하기.
# 그걸 DFS로 순회해서 최저값을 찾기
# 이상하긴 해. 그럴거면 애초에 DFS를 쓰지...
# 다익스트라를 버려야 하나?
# 좀 어렵긴하다. 유효성도 체크해야되니까...
# 2단계 하나 더 풀고 생각해봐야되나?
# 이거에 너무 시간 쓰는거 같기도 하고