# 1일 때 1
# 2일 때 2
# 3일 때 5
# 4일 때 14
# 5일 때 42
# 6일 때 132
# 입력은 최대 1000개의 테스트케이스
import sys
input = sys.stdin.readline

for _ in range(1000):
    N = int(input())
    if N == 0:
        break
    DP = [0] * 31
    DP[1] = 1
    DP[2] = 2
    DP[3] = 5
    DP[4] = 14
    DP[5] = 42
    DP[6] = 132