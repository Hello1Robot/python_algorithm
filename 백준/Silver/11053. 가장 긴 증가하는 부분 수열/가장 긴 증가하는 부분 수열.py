from sys import stdin; input=stdin.readline
N = int(input())
nums = tuple(map(int,input().split()))
DP = [1] * N
for i in range(1,N):
    for j in range(i):
        if nums[i] > nums[j]:
            DP[i] = max(DP[i], DP[j]+1)

print(max(DP))