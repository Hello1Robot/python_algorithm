N, K = map(int,input().split())

DP = [1] + [0]*(N)
for i in range(1,K+1):
    for j in range(1,N+1):
        DP[j] = (DP[j] + DP[j-1])%1000000000

print(DP[N])