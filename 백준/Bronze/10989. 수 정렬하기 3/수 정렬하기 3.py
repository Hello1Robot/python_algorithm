from sys import stdin; input = stdin.readline


N = int(input())
nums = [0]*(10001)
for _ in range(N):
    a = int(input())
    nums[a] += 1

for i in range(10001):
    if nums[i]:
        for _ in range(nums[i]):
            print(i)
    