from sys import stdin; input=stdin.readline

N = int(input())

field = [[0]*101 for _ in range(101)]

# 왼쪽이랑 아래 주는데 그래프 뒤집어져있는거니까 상관없음
for _ in range(N):
    left , btm = map(int,input().split())
    for i in range(left, left+10):
        for j in range(btm, btm+10):
            field[i][j] = 1
cnt = 0

for i in range(101):
    for j in range(101):
        if field[i][j] == 1:
            for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
                ni, nj = i + di, j + dj
                if ni < 0 or ni > 100 or nj < 0 or nj > 100:
                    cnt += 1
                if field[ni][nj] == 0:
                    cnt += 1

print(cnt)
