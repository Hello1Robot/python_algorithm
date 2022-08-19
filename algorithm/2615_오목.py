def 가로(x,y,field):
    if y >= 15:
        return 0
    else:
        if field[x][y] == field[x][y+1] == field[x][y+2] == field[x][y+3] == field[x][y+4]:
            if y+5 < 19 and field[x][y+5] != field[x][y]:
                return field[x][y]
def 세로(y,x,field):
    if x >= 15:
        return 0
    else:
        if field[y][x] == field[y+1][x] == field[y+2][x] == field[y+3][x] == field[y+4][x]:
            if x+5 < 19 and field[y+5][x] != field[y][x]:
                return field[y][x]
def 대각선1(x,y,field):
    
      

# 여섯 알 이상이 연속적으로 놓인 경우에는 이긴 것이 아니다.
# 가로세로 단어넣는 그 문제랑 큰 차이 없는듯?
field = [list(map(int,input().split())) for _ in range(19)]

for i in range(19):
    for j in range(19):
        if field[i][j] == 1:
            