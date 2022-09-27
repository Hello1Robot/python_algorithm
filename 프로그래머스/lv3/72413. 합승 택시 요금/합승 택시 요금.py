def solution(n, s, a, b, fares):
    answer = 1000000000
    field = [[1000000000]*(n+1) for _ in range(n+1)]

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
    for i in range(1,n+1):
        cost = field[s][i] + field[i][a] + field[i][b]
        answer = min(answer,cost)

    return answer