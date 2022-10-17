import sys
input = sys.stdin.readline

INF = 10000000
N = int(input())
M = int(input())
field = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int,input().split())
    if field[a][b] > c:
        field[a][b] = c


for i in range(1,N+1):
    field[i][i] = 0

for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            field[a][b] = min(field[a][b], field[a][k]+field[k][b])

for i in range(N+1):
    for j in range(N+1):
        if field[i][j] == INF:
            field[i][j] = 0

for x in range(1,N+1):
    for y in range(1,N+1):
        if field[x][y] == INF:
            field[x][y] = 0
        print(field[x][y], end=' ')
    print()

