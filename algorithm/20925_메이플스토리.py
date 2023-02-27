from sys import stdin; input=stdin.readline
N, T = map(int,input().split())
enter = []
exe = []
for _ in range(N):
    c, e = map(int,input().split())
    enter.append(c)
    exe.append(e)

move = [list(map(int,input().split())) for _ in range(N)]

DP = [[-1]*N for _ in range(T+1)]

for i in range(N):
    if not enter[i]:
        DP[0][i] = 0

for t in range(1, T + 1):
    for i in range(N):
        if DP[t-1][i] > -1:
            DP[t][i] = DP[t-1][i] + exe[i]
    for j in range(N):
        if i != j and t - move[j][i] >= 0 and DP[t - move[j][i]][j] >= enter[i]:
            DP[t][i] = max(DP[t][i], DP[t-move[j][i]][j])

print(max(DP[-1]))