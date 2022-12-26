N = int(input())
DP = [0]*(N+4)
# 홀수일 때는 못채움
if N % 2:
    print(0)
else:
    DP[2] = 3
    DP[4] = 11
    for i in range(6,N+1,2):
        DP[i] = DP[i-2]*4 - DP[i-4]
    print(DP[N])

# DP[4] = 11인데
# 숫자 세다가 포기