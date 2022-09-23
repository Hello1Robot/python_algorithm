N = [0] + list(input())
ln = len(N)
M = [0] + list(input())
lm = len(M)
field = [[0]*lm for _ in range(ln)]
max_cnt = 0
for i in range(1,ln):
    for j in range(1,lm):
        if N[i] == M[j]:
            field[i][j] = field[i-1][j-1]+1
            if field[i][j] > max_cnt:
                max_cnt = field[i][j]
        else:
            field[i][j] = max(field[i-1][j], field[i][j-1])

print(max_cnt)
        