# 이건 이차원 리스트를 만들어서
# 가장 많은 유저가 모일 수 있는 지점 선정하여
# 해당 지점을 골랐을 때, 몇 명이 파킹할 수 있는지를
# 찾아내기
# 완전탐색임
# 애초에 두 개로 정해져있어서
# 옆에 노드 걸 흡수하는 순서를 어떻게 정해야될지 모르겠는데
# 이게 순열써가지고 다 만들어서 돌릴 순 있잖아
# 근데 그거 돌리면, 근처 인구를 빨아먹어서 리미트를 채울거잖아?
# 못채우면 걔 점수로 되는거고 뭐 그런건데
# 만약에 지금은 괜찮아 이게 순서대로 하면 1에서 2 뽑아내고 6 뽑아내고 순서로 되니까
# 이게 좀 어렵다

# 뭐가 틀린지 뻔히 아는데 구현을 못해서 화가나네,,,
# 진짜 문제점 다 아는데
# 다 알면 뭐하냐구
# 구현을 못하는데


from itertools import permutations

def solution(n, edges, users, d, limit):
    field = [[1e8]*(n) for _ in range(n)]
    for start, end, dis in edges:
        if dis > d:
            continue
        field[start-1][end-1] = dis
        field[end-1][start-1] = dis
    

    for a in range(n):
        for b in range(n):
            if field[a][b] < 1e8:
                for c in range(n):
                    if a != c:
                        if field[a][b] + field[b][c] <= d:
                            field[a][c] = min(field[a][c], field[a][b] + field[b][c])

    answer = 0
    perms = list(permutations(range(n), 2))
    for x, y in perms:
        user = users[:]
        x_point = user[x]
        y_point = user[y]
        if x_point > limit:
            x_point = limit
        if y_point > limit:
            y_point = limit
        user[x] -= x_point
        user[y] -= y_point
        for j in range(n):
            if field[x][j] < 1e8:
                while x_point < limit and user[j] > 0:
                    user[j] -= 1
                    x_point += 1
            if field[y][j] < 1e8:
                while y_point < limit and user[j] > 0:
                    user[j] -= 1
                    y_point += 1

        answer = max(answer, x_point+y_point)                    

    return answer

print(solution(10,[[1,2,1],[1,3,1],[2,4,1],[3,5,1],[2,6,1],[4,5,1],[5,7,1],[5,8,1],[8,9,1],[9,10,1]],[1,3,5,7,9,11,13,15,17,19],10,30))


