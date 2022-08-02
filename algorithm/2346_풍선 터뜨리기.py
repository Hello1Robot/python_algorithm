N = int(input())

DP = [1] * N

memo = list(map(int, input().split()))
for i in memo:
    DP[0] = 0
    
