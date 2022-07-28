N = int(input())

# 1개 3개 4개 중 선택해서 가져갈 수 있음
# 돌의 갯수마다 win 과 lose를 알 수 있음
# 
# 효율적으로 진행할 경우.

DP = [1001] * (N+5)
DP[0] = 0
DP[1] = 0
DP[2] = 1
DP[3] = 0
DP[4] = 0


for i in range(5, N+1):
    if DP[i-1] or DP[i-3] or DP[i-4] == 1:
        DP[i] = 0
    else:
        DP[i] = 1

if DP[N] == 0:
    print('SK')
else:
    print('CY')