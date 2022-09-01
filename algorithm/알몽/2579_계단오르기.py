# 한 번에 한 계단씩 혹은 두 계단씩 오를 수 있음
# 연속된 세 개의 계단을 모두 밟으면 안 됨
# 그래서, 밟으면 연속 두개를 밟게 됨
# 그럼 '어느 계단을 밟지 않을 것인가'가 중요한 문제
# 3연속이 되지 않으려면, 어느 시점을 밟아야 효율적일까?
# 제약 조건 : 마지막 계단은 반드시 밟아야 함
import sys
input = sys.stdin.readline
N = int(input())
DP = [0] * (N+2)
nums = [int(input()) for _ in range(N)]
if N <= 2:
    print(sum(nums))
    exit()

# 어차피 마지막 계단을 밟아야 하면, 거꾸로 해도 괜찮지않나?
