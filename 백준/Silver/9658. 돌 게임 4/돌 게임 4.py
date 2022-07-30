N = int(input())

DP = [0] * (N+4)
DP[1] = 2
DP[2] = 1
DP[3] = 2
DP[4] = 1

for i in range(5, N+1):
    if DP[i-1] == 2 or DP[i-3] == 2 or DP[i-4] == 2:
        DP[i] = 1
    else:
        DP[i] = 2

print('SK') if DP[N] == 1 else print('CY')