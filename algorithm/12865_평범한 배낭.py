from sys import stdin; input = stdin.readline

N, K = map(int,input().split())

DP = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    weight, val = map(int,input().split())
    for j in range(1, K+1):
        if j < weight:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-weight] + val)
print(DP[N][K])