import copy
import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)

# 1년마다 카운트 없애는 함수 작성
# [1, -1, 0, 0] [0, 0, -1, 1]
def ice_break(x,y):
    sea_cnt = 0
    if (x-1) >= 0:
        if field[x-1][y] == 0:
            sea_cnt += 1
    if (x+1) < N:
        if field[x+1][y] == 0:
            sea_cnt += 1
    if (y-1) >= 0:
        if field[x][y-1] == 0:
            sea_cnt += 1
    if (y+1) < M:
        if field[x][y+1] == 0:
            sea_cnt += 1
    field[x][y] -= sea_cnt
    if field[x][y] < 0:
        field[x][y] = 0

# 카운트를 없앤 이후, 두 개로 떨어졌는지 확인하는 함수 작성
x_move = [-1, 1, 0, 0]
y_move = [0, 0, -1, 1]

def check_ice(m,n):
    check_field[m][n] = 0

    for x in range(4):
        if (m+x_move[x]) >=0 and (m+x_move[x]) < N and (n+y_move[x] >=0) and (n+y_move[x]) < M:
            new_n = check_field[m+x_move[x]][n+y_move[x]]
            if new_n != 0:
                check_ice(m+x_move[x],n+y_move[x])



N, M = map(int, input().split())
field = []
for _ in range(N):
    a = list(map(int, input().split()))
    field.append(a)


# 만약 모든 필드가 0이 된다면 0을 출력 X - 카운트가 0이면 0을 출력
ice_cnt = 0
while True:
    for i in range(N):
        for j in range(M):
            ice_break(i,j)
    ice_cnt += 1
    check_field = copy.deepcopy(field)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if check_field[i][j] == 0:
                continue
            else:
                check_ice(i,j)
                cnt+=1
    if cnt >= 2:
        print(ice_cnt)
        break
    elif cnt == 1:
        cnt = 0
        continue
    else:
        print(0)
        break