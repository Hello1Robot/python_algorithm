def check_left(x,y):
    if y-1 >= 0: # 범위를 벗어나지 않을 경우
        if field[x][y-1] == '.' and field[x+1][y-1] == '.':
            return True
    return False

def check_right(x,y):
    if y+1 < Y: # 범위를 벗어나지 않을 경우
        if field[x][y+1] == '.' and field[x+1][y+1] == '.':
            return True
    return False

X, Y = map(int,input().split())

field = [list(input()) for _ in range(X)]

# 양쪽이 벽일 경우를 생각하기. (인덱스범위)

N = int(input())
for case in range(N):
    stone = int(input())-1
    x = 0
    while x<X-1:
        if field[x+1][stone] == '.':
            x += 1
        elif field[x+1][stone] == 'X':
            field[x][stone] = 'O'
            break
        elif field[x+1][stone] == 'O':
            if check_left(x, stone):
                stone -= 1
                x += 1
            else:
                if check_right(x, stone):
                    stone += 1
                    x += 1
                else:
                    field[x][stone] = 'O'
                    break
        if x == X-1:
            field[x][stone] = 'O'
for line in field:
    print(*line)