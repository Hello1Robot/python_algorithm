from sys import stdin; input = stdin.readline

N = int(input())
nums = []
for _ in range(N):
    x, y = map(int,input().split())
    nums.append((x+y, x, y))

nums.sort()
print(abs(nums[0][1]-nums[-1][1])+abs(nums[0][2] - nums[-1][2]))