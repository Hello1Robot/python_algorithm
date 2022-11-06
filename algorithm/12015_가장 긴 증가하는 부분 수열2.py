import bisect # 이진탐색

N = int(input())
nums = tuple(map(int,input().split()))
DP = [nums[0]]

for i in range(N):
    if nums[i] > DP[-1]:
        DP.append(nums[i])
    else:
        now = bisect.bisect_left(DP, nums[i])
        DP[now] = nums[i]

print(len(DP))