from sys import stdin; input=stdin.readline

N = int(input())
K = int(input())
nums = list(map(int,input().split()))
nums.sort()
gaps = [0]*(N+1)
for i in range(1,N):
    gaps[i] = abs(nums[i-1]-nums[i])

gaps.sort()
while gaps and K != 1:
    gaps.pop()
    K -= 1

print(sum(gaps))
