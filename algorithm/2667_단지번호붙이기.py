def danji(m,n,cnt):
    field[m][n] = 0
    x_move = [-1, 1, 0, 0]
    y_move = [0, 0, -1, 1]
    for x in range(4):
        if (m+x_move[x]) >=0 and (m+x_move[x]) < N and (n+y_move[x] >=0) and (n+y_move[x]) < N:
            new_n = field[m+x_move[x]][n+y_move[x]]
            if new_n == 1:
                danji(m+x_move[x],n+y_move[x])
                cnt += 1
            else:
                continue
    return cnt


N = int(input())

field = [[map(int, input().split())] for _ in range(N)]
res_list = []
# 각 축 이동별 배열 (방향키로 움직이는 것과 비슷)

for i in range(N):
    for j in range(N):
        if field[i][j] == 0:
            continue
        else:
            res_list.append(danji(i,j,1))

print(*res_list)
 