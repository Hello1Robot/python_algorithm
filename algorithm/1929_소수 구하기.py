N, M = map(int, input().split())

DP = [0] * (M+1)
DP[0] = -1
DP[1] = -1
for i in range(2, M+1):
    n = 2
    if DP[i] == 0:
        while True:
            a = i * n
            if a > M:
                break
            else:
                DP[a] = 1
            n+=1
for x in range(N, M+1):
    if DP[x] == 0:
        print(x)