field = [[0]*101 for _ in range(101)]
cnt = 0
for i in range(4):
    x1, y1, x2, y2 = map(int,input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            if field[x][y] == 0:
                cnt += 1
            field[x][y] = 1

print(cnt)
            

