from sys import stdin; input=stdin.readline

N, M = map(int,input().split())
real = N*M
nums = tuple(map(int,input().split()))
for num in nums:
    print(num-real, end=' ')