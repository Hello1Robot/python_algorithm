mx = 5000001
N, M = map(int,input().split())
field = [[mx]*(N+1) for _ in range(N+1)]
min_tot = mx
res = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j:
            field[i][j] = 0

for _ in range(M):
    a, b = map(int,input().split())
    field[a][b] = 1
    field[b][a] = 1

for k in range(1, N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            field[i][j] = min(field[i][j], field[i][k] + field[k][j])

for i in range(1,N+1):
    tot = sum(field[i])-mx
    if tot < min_tot:
        min_tot = tot
        res = i
print(res)