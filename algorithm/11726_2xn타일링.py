N = int(input())
DP = [0]*(N+3)
DP[1] = 1
DP[2] = 2
for i in range(3, N+1):
    DP[i] = DP[i-1]+DP[i-2]

print(DP[N])