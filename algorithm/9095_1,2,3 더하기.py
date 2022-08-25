# DP문제
# 동전 1 응애버전
# 아니네 순열이네...
T = int(input())
for _ in range(T):
    N = int(input())
    DP = [1] * (N+1)
    for i in range(2, N+1):
        DP[i] += DP[i-2]
    for i in range(3, N+1):
        DP[i] += DP[i-3]        
    print(DP[N])