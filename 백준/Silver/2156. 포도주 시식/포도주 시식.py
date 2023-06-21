# 오랜만에 보는 DP 문제
# 3개 연속으로 못 먹는다는 조건만 있어서, 조건 설정이 어렵지는 않을 듯?
# 첫번째와 두 번째는 그냥 넣어두고, 나머지 올라가면서 확인하기
from sys import stdin; input = stdin.readline

N = int(input())
wines = [int(input()) for _ in range(N)]
if N <= 2:
    print(sum(wines))
    exit()


DP = [0] * N
DP[0] = wines[0]
DP[1] = wines[0]+wines[1]
DP[2] = max(wines[0]+wines[1], wines[1]+wines[2], wines[0]+wines[2])

for i in range(3,N):
    DP[i] = max(DP[i-2]+wines[i], DP[i-3]+wines[i], DP[i-3]+wines[i-1]+wines[i], DP[i-1])

print(max(DP[N-1],DP[N-2]))
