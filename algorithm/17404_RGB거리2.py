from sys import stdin
input = stdin.readline
N = int(input())
field = [tuple(map(int,input().split())) for _ in range(N)]
line1 = [0] * (N+1)
line2 = [0] * (N+1)
line3 = [0] * (N+1)
for i in range(2,N):
    line1[i] = min(line2[i-1], line3[i-1])+field[i-1][0]
    line2[i] = min(line1[i-1], line3[i-1])+field[i-1][1]
    line3[i] = min(line1[i-1], line2[i-1])+field[i-1][2]

print(min(line1[N-1]+field[N-1][1],
        line1[N-1]+field[N-1][2],
        line2[N-1]+field[N-1][0],
        line2[N-1]+field[N-1][2],
        line3[N-1]+field[N-1][0],
        line3[N-1]+field[N-1][1]))