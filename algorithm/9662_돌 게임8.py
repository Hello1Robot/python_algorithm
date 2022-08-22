import sys
input = sys.stdin.readline
# 돌 N개가 주어짐
# 돌을 가져갈 수 있는 방법 K가 주어짐
# 돌을 가져갈 수 있는 방법들이 주어짐
N = int(input())
DP = [0] * (N+500)
K = int(input())
nums = list(map(int, input().split()))
for num in nums:
    DP[num] = 1
# 갯수만큼 가져가지 못할 경우 지는 게임
# 창영이가 후공 - 창영이가 이길 경우의 수
for i in range(1,N+1):
    