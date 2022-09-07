import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    DP = [0] * (N+2)
    DP[0] = (1,0,)
    DP[1] = (0,1,)
    for i in range(2,N+1):
        a = DP[i-2][0] + DP[i-1][0]
        b = DP[i-2][1] + DP[i-1][1]
        DP[i] = (a,b,)
    print(DP[N][0], DP[N][1])