from sys import stdin; input=stdin.readline
N = int(input())
nums = list(map(int,input().split()))
nums.sort()
res = 0

for i in range(N):
    y = sum(nums[i+1:])
    res += nums[i]*y

print(res)
