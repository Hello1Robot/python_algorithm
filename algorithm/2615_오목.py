def 가로(x,y,field):
    if y >= 15:
        return False
    else:
        if not 가로vis[x][y]:

            if field[x][y] == field[x][y+1] == field[x][y+2] == field[x][y+3] == field[x][y+4]:
                if y+5 < 19 and field[x][y+5] != field[x][y]:
                    return (x,y, field[x][y])
                elif y+5 == 19:
                    return (x,y, field[x][y])
                elif field[x][y+5] == field[x][y]:
                    for i in range(5):
                        가로vis[x][y+i] = 1


def 세로(y,x,field):
    if y >= 15:
        return False
    else:
        if not 세로vis[y][x]:
            for i in range(5):
                세로vis[y+i][x] = 1
            if field[y][x] == field[y+1][x] == field[y+2][x] == field[y+3][x] == field[y+4][x]:
                if x+5 < 19 and field[y+5][x] != field[y][x]:
                    return (y,x, field[y][x])
                elif x+5 == 19:
                    return (y,x, field[y][x])
                elif field[y+5][x] == field[y][x]:
                    for i in range(5):
                        세로vis[y+i][x] = 1
def 대각선1(x,y,field):
    if x >= 15 or y >= 15:
        return False
    else:
        if not 대각1vis[x][y]:

            if field[x][y] == field[x+1][y+1] == field[x+2][y+2] == field[x+3][y+3] == field[x+4][y+4]:
                if x+5 < 19 and y+5 < 19 and field[x+5][y+5] != field[x][y]:
                    return (x,y, field[x][y])
                elif x+5 == 19 and y+5 == 19:
                    return (x,y, field[x][y])
                elif field[x+5][y+5] == field[x][y]:
                    for i in range(5):
                        대각1vis[x+i][y+i] = 1

def 대각선2(x,y,field):
    if x < 4 or y >= 15:
        return False
    else:
        if not 대각2vis[x][y]:

            if field[x][y] == field[x-1][y+1] == field[x-2][y+2] == field[x-3][y+3] == field[x-4][y+4]:
                if x-5 > 0 and y+5 < 19 and field[x-5][y+5] != field[x][y]:
                    return (x,y, field[x][y])
                elif x == 5 and y == 14:
                    return (x,y, field[x][y])
                elif field[x-5][y+5] != field[x][y]:
                    for i in range(5):
                        대각2vis[x-i][y+i] = 1



# 여섯 알 이상이 연속적으로 놓인 경우에는 이긴 것이 아니다.
# 가로세로 단어넣는 그 문제랑 큰 차이 없는듯?
field = [list(map(int,input().split())) for _ in range(19)]
가로vis = [[0]*19 for _ in range(19)]
세로vis = [[0]*19 for _ in range(19)]
대각1vis = [[0]*19 for _ in range(19)]
대각2vis = [[0]*19 for _ in range(19)]

for i in range(19):
    for j in range(19):
        if field[i][j]:
            a = 가로(i,j,field)
            b = 세로(i,j,field)
            c = 대각선1(i,j,field)
            d = 대각선2(i,j,field)
            if a:
                print(a[2])
                print(a[0]+1, a[1]+1)
                exit()
            if b:
                print(b[2])
                print(b[0]+1, b[1]+1)
                exit()
            if c:
                print(c[2])
                print(c[0]+1, c[1]+1)
                exit()
            if d:
                print(d[2])
                print(d[0]+1, d[1]+1)
                exit()
print(0)