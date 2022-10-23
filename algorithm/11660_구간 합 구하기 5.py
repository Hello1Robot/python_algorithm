import sys
input = sys.stdin.readline

N, M = map(int,input().split())

field = [list(map(int,input().split())) for _ in range(N)]

DP = [[0]*N for _ in range(N)]
tot = 0
for i in range(N):
    for j in range(N):
        tot += field[i][j]
        DP[i][j] = tot

for _ in range(M):
    x1, y1, x2, y2 = map(int,input().split())
    if x1 == 1 and y1 == 1:
        print(DP[x2-1][y2-1])
    elif x2==x1 and y2==y1:
        print(field[x1-1][y1-1])
    else:
        print(DP[x2-1][y2-1]-DP[x1-1][y1-1])