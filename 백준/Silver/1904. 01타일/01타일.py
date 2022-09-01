N = int(input())
DP = [0] * (N+5)
DP[1] = 1
DP[2] = 2
DP[3] = 3
DP[4] = 5
DP[5] = 8 # 피보나치구나
if N < 6:
    print(DP[N])
    exit()
for i in range(6,N+1):
    DP[i] = (DP[i-2]+DP[i-1])%15746

print(DP[N])