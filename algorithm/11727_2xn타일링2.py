N = int(input())
DP = [0]*(N+1)
DP[1] = 1
for i in range(2, N+1):
    if i % 2:
        DP[i] = (DP[i-1] * 2) -1
    else:
        DP[i] = (DP[i-1]*2) +1
print(DP[N]%10007)
