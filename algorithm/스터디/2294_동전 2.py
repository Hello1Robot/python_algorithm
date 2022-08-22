N, M = map(int, input().split())
coins = [int(input()) for _ in range(N)]
DP = [10001] * (M+1)
for coin in coins:
    if coin <= M:
        DP[coin] = 1

for i in range(M+1):
    mins = []
    mins.append(DP[i])
    for coin in coins:
        if i-coin > 0 and DP[i-coin] != 10001:
            mins.append(DP[i-coin]+1)
    if mins:
        DP[i] = min(mins)
if DP[M] == 10001:
    DP[M] = -1
print(DP[M])