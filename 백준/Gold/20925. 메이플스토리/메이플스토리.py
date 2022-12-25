import sys; input = sys.stdin.readline

N, T = map(int, input().split())
C = []
E = []
for _ in range(N):
    c, e = map(int, input().split())
    C.append(c)
    E.append(e)
move = [list(map(int, input().split())) for _ in range(N)]


dp = [[-1] * N for _ in range(T + 1)]


for i in range(N):
    if not C[i]:
        dp[0][i] = 0

for t in range(1, T + 1):
    for i in range(N):
        if dp[t - 1][i] > -1:
            dp[t][i] = dp[t - 1][i] + E[i]
        for j in range(N):
            if i != j and t - move[j][i] >= 0 and dp[t - move[j][i]][j] >= C[i]:
                dp[t][i] = max(dp[t][i], dp[t - move[j][i]][j])

print(max(dp[-1]))