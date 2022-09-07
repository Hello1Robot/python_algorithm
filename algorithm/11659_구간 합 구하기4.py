import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int,input().split()))
for i in range(1,N):
    nums[i] += nums[i-1]

for _ in range(M):
    start, end = map(int,input().split())
    if start == 1:
        print(nums[end-1])
    else:
        print(nums[end-1] - nums[start-2])