field = [tuple(map(int,input().split())) for _ in range(9)]

max_val = -1
max_x = -1
max_y = -1
for i in range(9):
    for j in range(9):
        if field[i][j] > max_val:
            max_val = field[i][j]
            max_x = i
            max_y = j

print(max_val)
print(max_x+1, max_y+1)