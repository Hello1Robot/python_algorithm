

def solution(n, s, a, b, fares):
    answer = 0
    field = [[10000000]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                field[i][j] = 0

    for fare in fares:
        stt, end, cost = fare
        field[stt][end] = cost
        field[end][stt] = cost

    for k in range(1, n+1): # 경유지
        for x in range(1, n+1):
            for y in range(1, n+1):
                # 그냥 a에서 b로 가는 것과 a에서 k를 경유해서 b로 가는 것 비교
                # 만약 가지 못할경우 값이 무한대이므로 넘어갈 것
                field[x][y] = min(field[x][y], field[x][k] + field[k][y])

    answer = min(field[s][a]+field[a][b], field[s][a]+field[s][b], field[s][b]+field[b][a])


    return answer




# 노드 수 : n
# 출발 지점 : s
# a의 도착점 : a
# b의 도착점 : b
# A에서 C로 가는 최단 거리 구함 - A에서 D로 가는 최단거리 구함 - A에서 C를 거쳐 D를 가는 비용 구함 - A에서 D를 거쳐 C로 가는 비용 구함 - 셋 비교
print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))