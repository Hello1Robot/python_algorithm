from sys import stdin; input=stdin.readline

N = int(input())
# 첫번째는 1,2만 고려
# 두번째는 1,2,3 고려
# 세번째는 2,3 고려
field = [tuple(map(int,input().split())) for _ in range(N)]

# 어차피 이전 것만 참조하니 홀짝 확인해서 홀수일 때는 0번을, 짝수일 때는 1번을 확인해서 채우도록 구현해야 함
# 슬라이드 윈도우
max_dp, min_dp = [[0,0,0], [0,0,0]], [[0,0,0], [0,0,0]]

for i in range(1,N+1):
    if i % 2:
        min_dp[1][0] = min(min_dp[0][0], min_dp[0][1]) + field[i-1][0]
        min_dp[1][1] = min(min_dp[0][0], min_dp[0][1], min_dp[0][2]) + field[i-1][1]
        min_dp[1][2] = min(min_dp[0][2], min_dp[0][1]) + field[i-1][2]
        max_dp[1][0] = max(max_dp[0][0], max_dp[0][1]) + field[i-1][0]
        max_dp[1][1] = max(max_dp[0][0], max_dp[0][1], max_dp[0][2]) + field[i-1][1]
        max_dp[1][2] = max(max_dp[0][2], max_dp[0][1]) + field[i-1][2]
    else:
        min_dp[0][0] = min(min_dp[1][0], min_dp[1][1]) + field[i-1][0]
        min_dp[0][1] = min(min_dp[1][0], min_dp[1][1], min_dp[1][2]) + field[i-1][1]
        min_dp[0][2] = min(min_dp[1][2], min_dp[1][1]) + field[i-1][2]
        max_dp[0][0] = max(max_dp[1][0], max_dp[1][1]) + field[i-1][0]
        max_dp[0][1] = max(max_dp[1][0], max_dp[1][1], max_dp[1][2]) + field[i-1][1]
        max_dp[0][2] = max(max_dp[1][2], max_dp[1][1]) + field[i-1][2]

print(max(max_dp[N%2]), min(min_dp[N%2]))