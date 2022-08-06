def check_underbar(x,y):
    if x < 0 or x >= X:
        return False
    if field[x][y] == '|':
        field[x][y] = 0
        check_underbar(x-1, y)
        check_underbar(x+1, y)
        return True
    else:
        return False 

def check_bar(x,y):
    if y < 0 or y >= Y:
        return False
    if field[x][y] == '-':
        field[x][y] = 0
        check_bar(x, y+1)
        check_bar(x, y-1)
        return True
    else:
        return False   

X, Y = map(int, input().split())

field = [list(input()) for x in range(X)]

cnt = 0
    
for i in range(X):
    for j in range(Y):
        if field[i][j] == '|':
            check_underbar(i,j)
            cnt+=1
        elif field[i][j] == '-':
            check_bar(i,j)
            cnt+=1            

print(cnt)