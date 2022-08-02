N, M = map(int, input().split())
coins = [int(input) for _ in range(N)]
DP = [9999] * (N+1)
for coin in coins:
    DP[coin] = 1

def coin_search(n):
    mins = []
    for coin in coins:
        mins.append(DP[n-coin]+1)
    